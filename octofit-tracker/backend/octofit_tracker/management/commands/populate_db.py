from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Explicitly set 'id' for each model instance
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=45),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot', age=25),
            User(id=ObjectId(), email='crashoverride@hmhigh.edu', name='Dade', age=22),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', age=28),
        ]
        User.objects.bulk_create(users)

        teams = [
            Team(id=ObjectId(), name='Blue Team'),
            Team(id=ObjectId(), name='Gold Team'),
        ]
        Team.objects.bulk_create(teams)

        # Convert User instances to dictionaries for the 'user' field in Activity
        activities = [
            Activity(id=ObjectId(), user=users[0].__dict__, type='Cycling', duration=60),
            Activity(id=ObjectId(), user=users[1].__dict__, type='Crossfit', duration=120),
            Activity(id=ObjectId(), user=users[2].__dict__, type='Running', duration=90),
            Activity(id=ObjectId(), user=users[3].__dict__, type='Strength', duration=30),
            Activity(id=ObjectId(), user=users[4].__dict__, type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Convert Team instances to dictionaries for the 'team' field in Leaderboard
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=teams[0].__dict__, score=100),
            Leaderboard(id=ObjectId(), team=teams[1].__dict__, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
