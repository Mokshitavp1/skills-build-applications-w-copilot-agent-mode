from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} ({self.email})"
    class Meta:
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return f"{self.name} - Members: {', '.join(self.members)}"
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.type} ({self.duration} min)"
    class Meta:
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.points} points"
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name} ({self.difficulty})"
    class Meta:
        db_table = 'workouts'
