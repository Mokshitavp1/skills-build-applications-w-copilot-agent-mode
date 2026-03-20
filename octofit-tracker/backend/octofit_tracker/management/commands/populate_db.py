from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample users
        users = [
            {'email': 'ironman@marvel.com', 'name': 'Iron Man', 'team': 'marvel'},
            {'email': 'captainamerica@marvel.com', 'name': 'Captain America', 'team': 'marvel'},
            {'email': 'batman@dc.com', 'name': 'Batman', 'team': 'dc'},
            {'email': 'wonderwoman@dc.com', 'name': 'Wonder Woman', 'team': 'dc'},
        ]
        for u in users:
            User.objects.create(**u)

        # Sample teams
        Team.objects.create(name='marvel', members=['Iron Man', 'Captain America'])
        Team.objects.create(name='dc', members=['Batman', 'Wonder Woman'])

        # Sample activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-03-20')
        Activity.objects.create(user='Batman', type='cycle', duration=45, date='2026-03-19')

        # Sample leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Sample workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
