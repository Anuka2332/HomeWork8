from django.db import models

# Create your models here.
class certif(models.Model):
    picture = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    who = models.CharField(max_length=200)
    description = models.TextField(max_length=500)


    def __str__(self):
        return f"{self.name}_{self.who}"