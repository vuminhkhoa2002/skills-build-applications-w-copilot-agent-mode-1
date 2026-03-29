
from djongo import models

class User(models.Model):
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.username

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField(help_text='Duration in minutes')
	date = models.DateField()
	def __str__(self):
		return f"{self.user.username} - {self.activity_type}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	suggested_for = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Leaderboard(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return f"{self.team.name} - {self.score}"
