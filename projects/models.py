from django.db import models
from farms.models import Farm, Field
from users.models import CustomUser

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title