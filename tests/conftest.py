# tests/conftest.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Django root (contains manage.py)
DJANGO_ROOT = ROOT / "lexbrief"

# Add BOTH to PYTHONPATH
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(DJANGO_ROOT))
