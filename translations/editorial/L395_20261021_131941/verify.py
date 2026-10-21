"""verify.py — wrapper del gate generico `tools/batch_lot.py`."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call([sys.executable, os.path.join(HERE, '..', 'tools', 'batch_lot.py'), 'verify', HERE]))
