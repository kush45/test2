#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Register.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
<<<<<<< HEAD
<<<<<<< HEAD

    print("kush")
=======
    
    print("test")
>>>>>>> ae7234048c9ab846e00e25e015d1e23bc6889cfc
=======
    
    print("test")
>>>>>>> ae7234048c9ab846e00e25e015d1e23bc6889cfc
