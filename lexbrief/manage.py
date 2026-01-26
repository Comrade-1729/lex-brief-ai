#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This file explicitly fixes the Python path to ensure the project
runs correctly regardless of the working directory.
"""

import os
import sys
from pathlib import Path


def main() -> None:
    # Absolute path to the directory containing manage.py
    base_dir = Path(__file__).resolve().parent

    # Ensure project root is on PYTHONPATH
    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))

    # Explicit Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lexbrief.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. "
            "Make sure it is installed and your virtual environment is activated."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
