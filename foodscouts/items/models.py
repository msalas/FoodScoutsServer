from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

    
	


