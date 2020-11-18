from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name