"""check.py — wrapper: questo lotto usa il gate generico `tools/batch_lot.py` (modalità batch)."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'tools', 'batch_lot.py')
sys.exit(subprocess.call([sys.executable, TOOL, 'check', HERE]))
