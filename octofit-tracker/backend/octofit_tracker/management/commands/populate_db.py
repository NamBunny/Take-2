from pymongo import MongoClient
from bson import ObjectId
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test inserting a single document into the users collection'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop the users collection
        db.users.drop()

        # Insert a single user document
        user = {"_id": ObjectId(), "username": "testuser", "email": "testuser@example.com", "password": "testpassword"}
        db.users.insert_one(user)

        self.stdout.write(self.style.SUCCESS('Successfully inserted a test user into the database.'))