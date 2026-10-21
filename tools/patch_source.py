#!/usr/bin/env python3
"""Produce the UTF-8 font patch for Endless Sky, without touching the repo.

Strategy
--------
Text substitution with **assertions**: every replacement must match the original
file exactly, otherwise the script aborts. The modified copies go to
`output/src/`, and a unified diff is written to `patches/0001-font-utf8.patch`
so a developer can review and apply it with `git apply`.

What it changes
---------------
* `Font.h`  : GLYPHS 98 -> 224, Glyph() takes char32_t.
* `Font.cpp`: Glyph() maps U+0020..U+00FF 1:1; DrawAliased() and WidthRawString()
  decode UTF-8 instead of iterating bytes.

The accent glyphs themselves come from `tools/font_extend.py` (extended atlas).
Nothing here has been compiled: the environment has no C++ toolchain.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = r"C:\Users\Dave\PROGETTI\G-DEV\GAME-SOURCE-LAB\endless-sky"

HELPER = '''using namespace std;

namespace {
\t// Decode one UTF-8 sequence and advance the pointer. Invalid or truncated
\t// sequences degrade to '?' instead of producing a random glyph cell.
\tchar32_t NextCodePoint(const char *&p) noexcept
\t{
\t\tconst unsigned char b = static_cast<unsigned char>(*p);
\t\tif(b < 0x80)
\t\t{
\t\t\t++p;
\t\t\treturn b;
\t\t}
\t\tif((b >> 5) == 0x6 && p[1])
\t\t{
\t\t\tconst char32_t c = ((b & 0x1F) << 6) | (p[1] & 0x3F);
\t\t\tp += 2;
\t\t\treturn c;
\t\t}
\t\tif((b >> 4) == 0xE && p[1] && p[2])
\t\t{
\t\t\tconst char32_t c = ((b & 0x0F) << 12) | ((p[1] & 0x3F) << 6) | (p[2] & 0x3F);
\t\t\tp += 3;
\t\t\treturn c;
\t\t}
\t\t// 4-byte sequences (emoji, rare scripts) are not in the atlas.
\t\tif((b >> 3) == 0x1E && p[1] && p[2] && p[3])
\t\t{
\t\t\tp += 4;
\t\t\treturn '?';
\t\t}
\t\t++p;
\t\treturn '?';
\t}
}
'''

REPLACEMENTS = {
    "Font.h": [
        ("\tstatic const int GLYPHS = 98;",
         "\t// 224 cells: ASCII 32..129 plus Latin-1 (U+00A0..U+00FF).\n\tstatic const int GLYPHS = 224;"),
        ("\tstatic int Glyph(char c, bool isAfterSpace) noexcept;",
         "\tstatic int Glyph(char32_t c, bool isAfterSpace) noexcept;"),
    ],
    "Font.cpp": [
        ("using namespace std;\n", HELPER),
        ("""int Font::Glyph(char c, bool isAfterSpace) noexcept
{
\t// Curly quotes.
\tif(c == '\\'' && isAfterSpace)
\t\treturn 96;
\tif(c == '"' && isAfterSpace)
\t\treturn 97;

\treturn max(0, min(GLYPHS - 3, c - 32));
}""",
         """int Font::Glyph(char32_t c, bool isAfterSpace) noexcept
{
\t// Curly quotes.
\tif(c == '\\'' && isAfterSpace)
\t\treturn 96;
\tif(c == '"' && isAfterSpace)
\t\treturn 97;

\t// The extended atlas maps U+0020..U+00FF one to one onto its cells.
\tif(c >= 32 && c <= 255)
\t\treturn static_cast<int>(c) - 32;
\t// Anything outside Latin-1 renders as '?' rather than as a wrong glyph.
\treturn '?' - 32;
}"""),
        ("""\tfor(char c : str)
\t{
\t\tif(c == '_')""",
         """\tfor(const char *p = str.c_str(); *p; )
\t{
\t\tconst char32_t c = NextCodePoint(p);
\t\tif(c == '_')"""),
        ("""\tfor( ; *str; ++str)
\t{
\t\tif(*str == '_')
\t\t\tcontinue;

\t\tint glyph = Glyph(*str, isAfterSpace);
\t\tif(*str != '"' && *str != '\\'')
\t\t\tisAfterSpace = !glyph;""",
         """\tfor(const char *p = str; *p; )
\t{
\t\tconst char32_t c = NextCodePoint(p);
\t\tif(c == '_')
\t\t\tcontinue;

\t\tint glyph = Glyph(c, isAfterSpace);
\t\tif(c != '"' && c != '\\'')
\t\t\tisAfterSpace = !glyph;"""),
    ],
}


def main() -> int:
    out_src = os.path.join(WS, "output", "src", "source", "text")
    os.makedirs(out_src, exist_ok=True)
    os.makedirs(os.path.join(WS, "patches"), exist_ok=True)

    originals = {}
    modified = {}
    eols = {}
    for name in ("Font.h", "Font.cpp"):
        src = os.path.join(REPO, "source", "text", name)
        raw = open(src, encoding="utf-8", newline="").read()
        eols[name] = "\r\n" if "\r\n" in raw else "\n"
        originals[name] = raw
        # match on LF-normalised text, restore the original endings on write
        text = raw.replace("\r\n", "\n")
        for old, new in REPLACEMENTS[name]:
            if old not in text:
                print(f"ABORT: pattern not found in {name}:\n{old[:120]}")
                return 2
            text = text.replace(old, new, 1)
        modified[name] = text

    # sanity assertions on the result
    checks = {
        "GLYPHS 224": "GLYPHS = 224" in modified["Font.h"],
        "char32_t glyph": "Glyph(char32_t c" in modified["Font.h"]
                          and "int Font::Glyph(char32_t c" in modified["Font.cpp"],
        "utf8 helper": "NextCodePoint(const char" in modified["Font.cpp"],
        "no byte loop in draw": "for(char c : str)" not in modified["Font.cpp"],
        "no byte loop in width": "for( ; *str; ++str)" not in modified["Font.cpp"],
    }
    for label, ok in checks.items():
        print(("PASS " if ok else "FAIL ") + label)
    if not all(checks.values()):
        return 1

    for name, text in modified.items():
        dst = os.path.join(out_src, name)
        with open(dst, "w", encoding="utf-8", newline="") as fh:
            fh.write(text.replace("\n", eols[name]))

    # unified diff per file, concatenated
    patch_path = os.path.join(WS, "patches", "0001-font-utf8.patch")
    parts = []
    for name in ("Font.h", "Font.cpp"):
        a = os.path.join(REPO, "source", "text", name)
        b = os.path.join(out_src, name)
        rel_a = f"a/source/text/{name}"
        rel_b = f"b/source/text/{name}"
        proc = subprocess.run(["diff", "-u", "--label", rel_a, "--label", rel_b, a, b],
                              capture_output=True, text=True)
        parts.append(proc.stdout)
    header = ("Subject: [PATCH] text: UTF-8 font rendering with a 224-cell Latin-1 atlas\n\n"
              "Font::Glyph() now takes a char32_t and maps U+0020..U+00FF onto the atlas;\n"
              "DrawAliased() and WidthRawString() decode UTF-8 instead of iterating bytes.\n"
              "Requires images/font/ubuntu{14,18}r_it.png generated by tools/font_extend.py\n"
              "(224 cells) copied over the original atlas, or GLYPHS must be reverted.\n\n")
    with open(patch_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header + "".join(parts))

    added = sum(1 for line in open(patch_path, encoding="utf-8")
                if line.startswith("+") and not line.startswith("+++"))
    print(f"\npatch: {patch_path} ({added} added lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
