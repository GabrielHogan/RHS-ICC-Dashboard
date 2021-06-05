from django.db import models

class Types(models.IntegerChoices):
    OTHER = -1, 'Other'

class Event(models.Model):
    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_virutal = models.BooleanField(default=False)
    type = models.IntegerField(choices=Types.choices, default=Types.OTHER)
    location = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return name