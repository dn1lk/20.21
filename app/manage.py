import os
import sys


def main():
    """Исполнение команд из консоли."""

    os.environ['DJANGO_SETTINGS_MODULE'] = "main.settings"

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
