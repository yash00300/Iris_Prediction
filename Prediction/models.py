from django.db import models

# Create your models here.

class Data(models.Model):
    
    sepalLengthCm = models.FloatField()
    sepalWidthCm = models.FloatField()
    petalLengthCm = models.FloatField()
    petalWidthCm = models.FloatField()
    
    species = models.IntegerField(null=True, blank= True)
    
    def __str__(self):
        return f'{self.id} {self.species}'
            