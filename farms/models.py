from django.db import models

class Farm(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Field(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Crop(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    harvest_date = models.DateField()

    def __str__(self):
        return self.name