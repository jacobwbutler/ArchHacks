from django.db import models

# Create your models here.
class Doctor(models.Model):
	full_name = models.CharField(max_length=200)

class Adherence(models.Model):
	target_times = models.DateTimeField()
	taken_times = models.DateTimeField(null=True)
	taken = models.BooleanField()

class Rx(models.Model):
	size = models.IntegerField()
	info = models.TextField()
	date_prescribed = models.DateField()
	active = models.BooleanField(default=True)
	drug = models.CharField(max_length=100)
	adherence = models.ForeignKey(Adherence, on_delete=models.CASCADE, null=True)

class Note(models.Model):
	time_entered = models.DateTimeField()
	description = models.TextField()

class Case(models.Model):
	active = models.BooleanField(default=True)
	rxs = models.ForeignKey(Rx, on_delete=models.CASCADE)
	notes = models.ForeignKey(Note, on_delete=models.CASCADE)

class Patient(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	cases = models.ForeignKey(Case, on_delete=models.CASCADE)
	