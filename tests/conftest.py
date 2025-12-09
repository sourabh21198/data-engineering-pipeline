# tests/conftest.py
import sys
from pathlib import Path

# project root -> one level up from tests/
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

# put src at front of sys.path so "import src..." works
sys.path.insert(0, str(SRC))
