from pymongo import MongoClient
from bson import ObjectId
from django.conf import settings
from django.core.management.base import BaseCommand
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboards.drop()
        db.workouts.drop()

        # Insert test users
        users = [
            {"_id": ObjectId(), "username": "user1", "email": "user1@example.com", "password": "password1"},
            {"_id": ObjectId(), "username": "user2", "email": "user2@example.com", "password": "password2"},
            {"_id": ObjectId(), "username": "user3", "email": "user3@example.com", "password": "password3"},
        ]
        db.users.insert_many(users)

        # Insert test teams
        teams = [
            {"_id": ObjectId(), "name": "Team A", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Team B", "members": [users[2]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Insert test activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": timedelta(hours=1).total_seconds()},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Cycling", "duration": timedelta(hours=2).total_seconds()},
        ]
        db.activities.insert_many(activities)

        # Insert test leaderboard entries
        leaderboards = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
        ]
        db.leaderboards.insert_many(leaderboards)

        # Insert test workouts
        workouts = [
            {"_id": ObjectId(), "name": "Workout A", "description": "Description A"},
            {"_id": ObjectId(), "name": "Workout B", "description": "Description B"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))