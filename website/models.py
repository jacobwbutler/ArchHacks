from django.db import models


# Create your models here.
class Doctor(models.Model):
    full_name = models.CharField(max_length=200)
    work_number = models.IntegerField()

    def __str__(self):
        return self.full_name


class Adherence(models.Model):
    taken_am = models.NullBooleanField(null=True)
    taken_midday = models.NullBooleanField(null=True)
    taken_pm = models.NullBooleanField(null=True)
    def percentage(self):
        counter = 0
        if taken_am: counter += 1
        if taken_midday: counter += 1
        if taken_pm: counter += 1
        return counter / 3

    def __str__(self):
        return "Adherence"


class Target(models.Model):
    weekdays = ["monday", "tuesday",
                "wednesday", "thursday",
                "friday", "saturday",
                "sunday"]
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()

    target_time_am = models.TimeField(null=True, blank=True)
    target_time_midday = models.TimeField(null=True, blank=True)
    target_time_pm = models.TimeField(null=True, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Target"

class Rx(models.Model):
    size = models.IntegerField()
    info = models.TextField()
    date_prescribed = models.DateField()
    active = models.BooleanField(default=True)
    drug = models.CharField(max_length=100)
    target = models.ForeignKey(Target, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.drug

class Note(models.Model):
    time_entered = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return str(self.time_entered) + " note."

class Case(models.Model):
    active = models.BooleanField(default=True)
    rxs = models.ForeignKey(Rx, on_delete=models.CASCADE)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return "Case"

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    cases = models.ForeignKey(Case,
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
