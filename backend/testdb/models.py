from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    position = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    time_spent = models.PositiveIntegerField(default=0)
# Create your models here.
