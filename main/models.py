from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Infra(models.Model):
    # fields for the Infra table
    name = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=800)
    description = models.TextField(max_length=5000)
    release_date = models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)
    electricity = models.FloatField()
    railways = models.TextField(max_length=1000)
    bridges = models.FloatField()
    tunnels = models.FloatField()
    water_supply = models.CharField(max_length=1)
    sewers = models.FloatField()
    telecommunication = models.TextField(max_length=5000)
    market = models.FloatField()
    transportation = models.TextField(max_length=5000)
    distributors = models.TextField(max_length=5000)
    suppliers = models.TextField(max_length=5000)
    mining_area = models.FloatField()
    forest_area = models.FloatField()
    ready_to_use_land = models.FloatField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Review(models.Model):
    Infra = models.ForeignKey(Infra, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
