from django.db import models

# Create your models here.

class Legislator(models.Model):
    PARTY = [('D', 'Democrat'), ('R', 'Republican'), ('L', 'Libertarian'), ('G', 'Green Party'), ('I', 'Independent')]
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    party = models.CharField(max_length=2, choices=PARTY, default='I')
