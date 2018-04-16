from django.db import models

# Create your models here.

class Legislator(models.Model):
    PARTY = [('D', 'Democrat'), ('R', 'Republican'), ('L', 'Libertarian'), ('G', 'Green Party'), ('I', 'Independent')]
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    party = models.CharField(max_length=2, choices=PARTY, default='I')
    identifier = models.CharField(max_length=9, default='NULL')

class Donation(models.Model):
    identifier = models.CharField(max_length=9)
    name = models.CharField(max_length=100)
    mean = models.DecimalField(max_digits=10, decimal_places=7)
    individual = models.IntegerField()
    pac = models.IntegerField()
    donoSetOne = models.IntegerField()
    donoSetTwo = models.IntegerField()
    donoSetThree = models.IntegerField()
    donoSetFour = models.IntegerField()
    donoSetFive = models.IntegerField()



