from django.db import models
from datetime import date


# Create your models here.

class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()
    # date = models.DateField(default=date.today())

    def __str__(self):
        return str(self.id) + "_" + str(self.title)
