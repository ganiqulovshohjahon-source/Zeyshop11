#!/usr/bin/env python
import importlib
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zayshop.settings")
    try:
        execute_from_command_line = importlib.import_module(
            "django.core.management"
        ).execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django o'rnatilmagan. Iltimos, avval pip orqali o'rnating."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
