from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test', type='Run', duration=10)
        self.assertEqual(str(activity), 'test - Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Test', points=100)
        self.assertEqual(str(lb), 'Test: 100')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushup', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushup (Easy)')
