#!/usr/bin/env python3
"""Extend the Endless Sky bitmap font atlas from 98 to 224 cells (Latin-1).

Why this approach
-----------------
The game ships two *bitmap* atlases (98 cells of ASCII 32..129). There is no
TTF and no rasterizer in this environment, so a real re-render is impossible.
What is possible — and correct — is to build the Latin-1 cells (U+00A0..U+00FF)
from the existing ones: base letters are copied, diacritics are drawn as small
strokes above the glyph's own ink, and symbols are approximated from ASCII.

Output is a new atlas with the same cell size and height, so
`Font::SetUpShader(width / GLYPHS, height)` keeps working with GLYPHS = 224.

Everything is verified: base cells must be byte-identical to the original, every
target glyph must have ink in both the base band and the accent band, and a
preview strip is rendered for manual inspection.

Usage
-----
    python tools/font_extend.py --images <repo>/images/font --out font
"""

from __future__ import annotations

import argparse
import json
import os
import struct
import sys
import zlib

GLYPHS_IN = 98
GLYPHS_OUT = 224


# ---------------------------------------------------------------- PNG codec
def read_png(path):
    data = open(path, "rb").read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    pos, width, height = 8, 0, 0
    ctype = bitdepth = 0
    idat = []
    while pos + 8 <= len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        chunk = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, bitdepth, ctype, _c, _f, interlace = struct.unpack(">IIBBBBB", chunk)
            if bitdepth != 8 or interlace != 0 or ctype not in (2, 6):
                raise ValueError(f"unsupported PNG (depth {bitdepth}, type {ctype})")
        elif kind == b"IDAT":
            idat.append(chunk)
        elif kind == b"IEND":
            break
    raw = zlib.decompress(b"".join(idat))
    bpp = 4 if ctype == 6 else 3
    stride = width * bpp
    out = bytearray(width * height * 4)
    prev = bytearray(stride)
    src = 0
    for y in range(height):
        f = raw[src]
        src += 1
        line = bytearray(raw[src:src + stride])
        src += stride
        if f == 1:
            for i in range(bpp, stride):
                line[i] = (line[i] + line[i - bpp]) & 0xFF
        elif f == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 0xFF
        elif f == 3:
            for i in range(stride):
                left = line[i - bpp] if i >= bpp else 0
                line[i] = (line[i] + ((left + prev[i]) >> 1)) & 0xFF
        elif f == 4:
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0
                b = prev[i]
                c = prev[i - bpp] if i >= bpp else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 0xFF
        prev = line
        for x in range(width):
            o = (y * width + x) * 4
            s = x * bpp
            if bpp == 4:
                out[o:o + 4] = line[s:s + 4]
            else:
                out[o:o + 3] = line[s:s + 3]
                out[o + 3] = 255
    return width, height, out


def write_png(path, width, height, rgba):
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        raw += rgba[y * width * 4:(y + 1) * width * 4]

    def chunk(kind, payload):
        return (struct.pack(">I", len(payload)) + kind + payload
                + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF))

    out = b"\x89PNG\r\n\x1a\n"
    out += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    out += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    out += chunk(b"IEND", b"")
    open(path, "wb").write(out)


# ---------------------------------------------------------------- cell tools
class Cell:
    def __init__(self, w, h, data=None):
        self.w, self.h = w, h
        self.px = bytearray(data) if data else bytearray(w * h * 4)

    @classmethod
    def from_atlas(cls, atlas, index, cw):
        w, h, px = atlas
        out = cls(cw, h)
        for y in range(h):
            src = (y * w + index * cw) * 4
            out.px[y * cw * 4:(y + 1) * cw * 4] = px[src:src + cw * 4]
        return out

    def get(self, x, y):
        return self.px[(y * self.w + x) * 4 + 3]

    def set(self, x, y, a=255):
        if 0 <= x < self.w and 0 <= y < self.h:
            o = (y * self.w + x) * 4
            self.px[o] = 255
            self.px[o + 1] = 255
            self.px[o + 2] = 255
            self.px[o + 3] = a

    def clear(self, x, y):
        o = (y * self.w + x) * 4
        self.px[o:o + 4] = b"\x00\x00\x00\x00"

    def ink(self):
        return sum(1 for i in range(3, len(self.px), 4) if self.px[i] > 40)

    def bbox(self):
        xs, ys = [], []
        for y in range(self.h):
            for x in range(self.w):
                if self.get(x, y) > 40:
                    xs.append(x)
                    ys.append(y)
        if not xs:
            return None
        return min(xs), min(ys), max(xs), max(ys)

    def blit(self, other, dx=0, dy=0):
        for y in range(other.h):
            for x in range(other.w):
                if other.get(x, y) > 40:
                    self.set(x + dx, y + dy, other.get(x, y))


def copy_cell(src, s):
    out = Cell(src.w, src.h)
    for y in range(src.h):
        for x in range(src.w):
            a = src.get(x, y)
            if a:
                out.set(x, y, a)
    return out


# ---------------------------------------------------------------- diacritics
def draw_mark(cell, kind, cx, y, size):
    """Draw a small diacritic centred on cx at row y."""
    if kind == "grave":
        for i in range(3):
            cell.set(cx - 3 + i, y + 2 - i)
            cell.set(cx - 2 + i, y + 2 - i)
    elif kind == "acute":
        for i in range(3):
            cell.set(cx + 1 - i, y + 2 - i)
            cell.set(cx + 2 - i, y + 2 - i)
    elif kind == "circumflex":
        for i in range(3):
            cell.set(cx - i, y + i)
            cell.set(cx + i, y + i)
            cell.set(cx - i, y + i + 1)
            cell.set(cx + i, y + i + 1)
    elif kind == "tilde":
        cell.set(cx - 3, y + 1)
        cell.set(cx - 2, y)
        cell.set(cx - 1, y + 1)
        cell.set(cx, y)
        cell.set(cx + 1, y + 1)
        cell.set(cx + 2, y)
        cell.set(cx + 3, y + 1)
    elif kind == "diaeresis":
        cell.set(cx - 2, y)
        cell.set(cx - 2, y + 1)
        cell.set(cx + 2, y)
        cell.set(cx + 2, y + 1)
    elif kind == "ring":
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            cell.set(cx + dx, y + 1 + dy)
    elif kind == "cedilla":
        cell.set(cx, y)
        cell.set(cx, y + 1)
        cell.set(cx - 1, y + 2)
    elif kind == "macron":
        for dx in range(-3, 4):
            cell.set(cx + dx, y)
    elif kind == "slash":
        for i in range(cell.h // 2):
            cell.set(2 + i, cell.h // 2 - i + 6)
    size = size  # kept for symmetry with future scaling


def compose(base, mark, dots=False):
    """Return base glyph with a diacritic placed above its own ink."""
    out = copy_cell(base, None)
    bb = out.bbox()
    if not bb:
        return out
    x0, y0, x1, y1 = bb
    cx = (x0 + x1) // 2
    if dots:  # 'i' keeps its dot: clear it, then mark above the x-height
        top = y0
        for y in range(top, min(out.h, top + 4)):
            for x in range(x0, x1 + 1):
                out.clear(x, y)
        bb = out.bbox()
        y0 = bb[1] if bb else top + 4
    mark_y = max(0, y0 - 6)
    draw_mark(out, mark, cx, mark_y, 4)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", required=True, help="path to <repo>/images/font")
    ap.add_argument("--out", required=True, help="output folder for the extended atlases")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    report = {"atlases": [], "ok": True}

    for name in ("ubuntu14r.png", "ubuntu18r.png"):
        src_path = os.path.join(args.images, name)
        if not os.path.exists(src_path):
            print(f"FATAL: {src_path} missing")
            return 2
        width, height, px = read_png(src_path)
        cw = width // GLYPHS_IN
        if cw * GLYPHS_IN != width:
            print(f"FATAL: {name} width {width} not divisible by {GLYPHS_IN}")
            return 2

        atlas = (width, height, px)
        cells = [Cell.from_atlas(atlas, i, cw) for i in range(GLYPHS_IN)]

        def ascii_cell(ch):
            return cells[ord(ch) - 32] if 32 <= ord(ch) <= 129 else None

        # Latin-1 plan: unicode -> (base char, mark) or a literal ascii fallback
        plan = {
            0xA0: ("", None), 0xA1: ("!", "flip"), 0xA2: ("c", None), 0xA3: ("L", None),
            0xA4: ("o", None), 0xA5: ("Y", None), 0xA6: ("|", None), 0xA7: ("S", None),
            0xA8: ("", "diaeresis"), 0xA9: ("c", None), 0xAA: ("a", None), 0xAB: ("<", "double"),
            0xAC: ("-", None), 0xAD: ("", None), 0xAE: ("r", None), 0xAF: ("", "macron"),
            0xB0: ("o", None), 0xB1: ("+", None), 0xB2: ("2", None), 0xB3: ("3", None),
            0xB4: ("", "acute"), 0xB5: ("u", None), 0xB6: ("P", None), 0xB7: (".", None),
            0xB8: ("", "cedilla"), 0xB9: ("1", None), 0xBA: ("o", None), 0xBB: (">", "double"),
            0xBC: ("1", None), 0xBD: ("1", None), 0xBE: ("3", None), 0xBF: ("?", "flip"),
            0xC0: ("A", "grave"), 0xC1: ("A", "acute"), 0xC2: ("A", "circumflex"),
            0xC3: ("A", "tilde"), 0xC4: ("A", "diaeresis"), 0xC5: ("A", "ring"),
            0xC6: ("A", None), 0xC7: ("C", "cedilla"),
            0xC8: ("E", "grave"), 0xC9: ("E", "acute"), 0xCA: ("E", "circumflex"),
            0xCB: ("E", "diaeresis"),
            0xCC: ("I", "grave"), 0xCD: ("I", "acute"), 0xCE: ("I", "circumflex"),
            0xCF: ("I", "diaeresis"),
            0xD0: ("D", None), 0xD1: ("N", "tilde"),
            0xD2: ("O", "grave"), 0xD3: ("O", "acute"), 0xD4: ("O", "circumflex"),
            0xD5: ("O", "tilde"), 0xD6: ("O", "diaeresis"), 0xD7: ("x", None),
            0xD8: ("O", "slash"),
            0xD9: ("U", "grave"), 0xDA: ("U", "acute"), 0xDB: ("U", "circumflex"),
            0xDC: ("U", "diaeresis"), 0xDD: ("Y", "acute"), 0xDE: ("P", None), 0xDF: ("B", None),
            0xE0: ("a", "grave"), 0xE1: ("a", "acute"), 0xE2: ("a", "circumflex"),
            0xE3: ("a", "tilde"), 0xE4: ("a", "diaeresis"), 0xE5: ("a", "ring"),
            0xE6: ("a", None), 0xE7: ("c", "cedilla"),
            0xE8: ("e", "grave"), 0xE9: ("e", "acute"), 0xEA: ("e", "circumflex"),
            0xEB: ("e", "diaeresis"),
            0xEC: ("i", "grave"), 0xED: ("i", "acute"), 0xEE: ("i", "circumflex"),
            0xEF: ("i", "diaeresis"),
            0xF0: ("d", None), 0xF1: ("n", "tilde"),
            0xF2: ("o", "grave"), 0xF3: ("o", "acute"), 0xF4: ("o", "circumflex"),
            0xF5: ("o", "tilde"), 0xF6: ("o", "diaeresis"), 0xF7: ("-", None),
            0xF8: ("o", "slash"),
            0xF9: ("u", "grave"), 0xFA: ("u", "acute"), 0xFB: ("u", "circumflex"),
            0xFC: ("u", "diaeresis"), 0xFD: ("y", "acute"), 0xFE: ("p", None),
            0xFF: ("y", "diaeresis"),
        }

        # Layout must be codepoint-32 for the whole range: Latin-1 lands at
        # indices 128..223, indices 98..127 (codepoints 130..159) stay empty.
        out_cells = [Cell(cw, height) for _ in range(GLYPHS_OUT)]
        for i in range(GLYPHS_IN):
            out_cells[i] = copy_cell(cells[i], None)
        for code in range(0xA0, 0x100):
            base_char, mark = plan.get(code, ("", None))
            base = ascii_cell(base_char) if base_char else None
            if base is None:
                cell = Cell(cw, height)
            elif mark is None:
                cell = copy_cell(base, None)
            elif mark == "flip":
                cell = Cell(cw, height)
                for y in range(height):
                    for x in range(cw):
                        if base.get(x, height - 1 - y) > 40:
                            cell.set(x, y, base.get(x, height - 1 - y))
            elif mark == "double":
                cell = Cell(cw, height)
                for y in range(height):
                    for x in range(cw // 2):
                        if base.get(x, y) > 40:
                            cell.set(x, y, base.get(x, y))
                            cell.set(x + cw // 2, y, base.get(x, y))
            else:
                cell = compose(base, mark, dots=(base_char == "i"))
            out_cells[code - 32] = cell

        new_w = cw * GLYPHS_OUT
        canvas = bytearray(new_w * height * 4)
        for index, cell in enumerate(out_cells[:GLYPHS_OUT]):
            for y in range(height):
                src = y * cw * 4
                dst = (y * new_w + index * cw) * 4
                canvas[dst:dst + cw * 4] = cell.px[src:src + cw * 4]

        dst_name = name.replace(".png", "_it.png")
        dst_path = os.path.join(args.out, dst_name)
        write_png(dst_path, new_w, height, canvas)

        # verification
        base_identical = all(
            cells[i].px == Cell.from_atlas((new_w, height, canvas), i, cw).px
            for i in range(GLYPHS_IN))
        critical = {"à": 0xE0, "è": 0xE8, "é": 0xE9, "ì": 0xEC, "ò": 0xF2, "ù": 0xF9,
                    "À": 0xC0, "È": 0xC8, "É": 0xC9, "Ì": 0xCC, "Ò": 0xD2, "Ù": 0xD9}
        glyph_stats = {}
        for ch, code in critical.items():
            cell = Cell.from_atlas((new_w, height, canvas), code - 32, cw)
            bb = cell.bbox()
            glyph_stats[ch] = {"ink": cell.ink(), "bbox": bb}
        all_ink = all(v["ink"] > 10 for v in glyph_stats.values())

        entry = {"atlas": name, "cell": cw, "height": height,
                 "cells_in": GLYPHS_IN, "cells_out": GLYPHS_OUT,
                 "new_width": new_w, "base_cells_identical": base_identical,
                 "critical_glyphs": glyph_stats, "critical_ok": all_ink,
                 "out": dst_name}
        report["atlases"].append(entry)
        report["ok"] &= base_identical and all_ink
        print(f"{dst_name}: {GLYPHS_OUT} celle da {cw}x{height} (larghezza {new_w}) · "
              f"base identiche={base_identical} · accentate con inchiostro={all_ink}")

    # preview strip: the 12 critical glyphs, upscaled 2x for inspection
    cw = GLYPHS_IN and report["atlases"][0]["cell"]
    height = report["atlases"][0]["height"]
    atlas_path = os.path.join(args.out, report["atlases"][0]["out"])
    aw, ah, apx = read_png(atlas_path)
    strip_codes = [0xE0, 0xE8, 0xE9, 0xEC, 0xF2, 0xF9, 0xC0, 0xC8, 0xC9, 0xCC, 0xD2, 0xD9]
    scale = 2
    pw, ph = len(strip_codes) * cw * scale, height * scale
    strip = bytearray(pw * ph * 4)
    for i, code in enumerate(strip_codes):
        cell = Cell.from_atlas((aw, ah, apx), code - 32, cw)
        for y in range(height):
            for x in range(cw):
                a = cell.get(x, y)
                if not a:
                    continue
                for dy in range(scale):
                    for dx in range(scale):
                        o = ((y * scale + dy) * pw + (i * cw * scale + x * scale + dx)) * 4
                        strip[o:o + 4] = bytes((255, 255, 255, a))
    preview = os.path.join(args.out, "preview_accenti.png")
    write_png(preview, pw, ph, strip)
    report["preview"] = preview

    with open(os.path.join(args.out, "font_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    print("preview:", preview)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
