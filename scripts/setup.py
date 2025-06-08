"""
To run the initial migration and create superuser:
"""
import os
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py createsuperuser')
"""
Run this file with `python scripts/setup.py`
"""
