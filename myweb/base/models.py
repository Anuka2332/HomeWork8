from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Who(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField
    data = models.DateField(null=True)

    def __str__(self):
        return self.name


class certif(models.Model):
    picture = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    who = models.ForeignKey(Who, on_delete=models.SET("Unknown Who"))
    description = models.TextField(max_length=500)


    def __str__(self):
        return f"{self.name}_{self.who}"


class User(AbstractUser):
    certifs = models.ManyToManyField(certif, blank=True, related_name="certifs")