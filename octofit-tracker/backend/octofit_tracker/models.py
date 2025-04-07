from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use 'id' for compatibility with Django
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        abstract = False  # Make the User model concrete

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use 'id' for compatibility with Django
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use 'id' for compatibility with Django
    user = models.EmbeddedField(model_container=User)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use 'id' for compatibility with Django
    team = models.EmbeddedField(model_container=Team)
    score = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use 'id' for compatibility with Django
    name = models.CharField(max_length=255)
    description = models.TextField()
