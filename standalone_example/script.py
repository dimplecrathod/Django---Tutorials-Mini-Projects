import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'standalone_example.settings')
django.setup()

from example.models import Person

new_person = Person(name='Dimple')
new_person.save()