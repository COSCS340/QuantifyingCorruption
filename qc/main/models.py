from django.db import models

# Create your models here.

class Legislator(models.Model):
    PARTY = [('D', 'Democrat'), ('R', 'Republican'), ('L', 'Libertarian'), ('G', 'Green Party'), ('I', 'Independent')]
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    party = models.CharField(max_length=2, choices=PARTY, default='I')
    identifier = models.CharField(max_length=9)
    mean = models.FloatField(default=0)
    median = models.FloatField(default=0)
    individual = models.FloatField(default=0)
    pac = models.FloatField(default=0)
    donoSetOne = models.FloatField(default=0)
    donoSetTwo = models.FloatField(default=0)
    donoSetThree = models.FloatField(default=0)
    donoSetFour = models.FloatField(default=0)
    donoSetFive = models.FloatField(default=0)
