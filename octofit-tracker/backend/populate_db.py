import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def create_users():
    users = []
    for i in range(5):
        user = User.objects.create(
            username=f'user{i+1}',
            email=f'user{i+1}@example.com'
        )
        users.append(user)
    return users

def create_teams(users):
    teams = []
    for i in range(2):
        team = Team.objects.create(name=f'Team{i+1}')
        for user in users[i*2:(i+1)*2+1]:
            team.members.add(user)
        team.save()
        teams.append(team)
    return teams

def create_workouts():
    workouts = []
    for i in range(3):
        workout = Workout.objects.create(
            name=f'Workout{i+1}',
            description=f'Description for workout {i+1}',
            suggested_for='General'
        )
        workouts.append(workout)
    return workouts

def create_activities(users):
    for user in users:
        for i in range(2):
            Activity.objects.create(
                user=user,
                activity_type=random.choice(['Run', 'Bike', 'Swim']),
                duration=random.randint(20, 60),
                date=date.today() - timedelta(days=i)
            )

def create_leaderboards(teams):
    for team in teams:
        Leaderboard.objects.create(
            team=team,
            score=random.randint(100, 500)
        )

def main():
    users = create_users()
    teams = create_teams(users)
    create_workouts()
    create_activities(users)
    create_leaderboards(teams)
    print('Test data created successfully!')

if __name__ == '__main__':
    main()
