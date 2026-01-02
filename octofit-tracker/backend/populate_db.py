import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Clear existing data
def clear_db():
    Leaderboard.objects.all().delete()
    Workout.objects.all().delete()
    Activity.objects.all().delete()
    Team.objects.all().delete()
    User.objects.all().delete()

def populate():
    # Create users
    user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
    user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Brown')
    user3 = User.objects.create(username='carol', email='carol@example.com', first_name='Carol', last_name='Jones')

    # Create teams
    team1 = Team.objects.create(name='Team Alpha')
    team2 = Team.objects.create(name='Team Beta')
    team1.members.set([user1, user2])
    team2.members.set([user3])

    # Create activities
    Activity.objects.create(user=user1, activity_type='run', duration=30, calories=250, date=datetime.date(2025, 12, 1))
    Activity.objects.create(user=user2, activity_type='bike', duration=45, calories=400, date=datetime.date(2025, 12, 2))
    Activity.objects.create(user=user3, activity_type='swim', duration=60, calories=500, date=datetime.date(2025, 12, 3))

    # Create workouts
    workout1 = Workout.objects.create(name='Cardio Blast', description='Intense cardio session', difficulty='Medium')
    workout2 = Workout.objects.create(name='Strength Builder', description='Strength training', difficulty='Hard')
    workout1.suggested_for.set([user1, user3])
    workout2.suggested_for.set([user2])

    # Create leaderboards
    Leaderboard.objects.create(team=team1, score=1200)
    Leaderboard.objects.create(team=team2, score=800)

if __name__ == '__main__':
    clear_db()
    populate()
    print('Base de données peuplée avec des données de test.')
