from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Suppression des anciennes données
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Création des équipes
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Création des utilisateurs
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel)

        # Création des activités
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)
        Activity.objects.create(user=superman, type='Swimming', duration=60)
        Activity.objects.create(user=spiderman, type='Yoga', duration=20)

        # Création des workouts
        Workout.objects.create(name='Full Body', description='Full body workout')
        Workout.objects.create(name='Cardio', description='Cardio session')

        # Création du leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)
        Leaderboard.objects.create(user=superman, score=95)
        Leaderboard.objects.create(user=spiderman, score=80)

        self.stdout.write(self.style.SUCCESS('octofit_db a été peuplée avec des données de test.'))
