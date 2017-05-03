from django.db import models


# Create your models here.
class Parking(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    capacity = models.IntegerField()
    latitude = models.FloatField(default=30.52)
    longitude = models.FloatField(default=30.30)

    def __str__(self):
        return 'Parking {} on {} places for {} uan'.format(self.title, self.capacity, self.price)
