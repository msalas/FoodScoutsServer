from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name
    def average_rating(self):
        return 10

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
	#user = models.ForeignKey(Users)
    item = models.ForeignKey(Item)
    def __unicode__(self):
        return self.rating
	
class Bookmark(models.Model):
	#user = models.ForeignKey(Users)
    item = models.ForeignKey(Item)
    def __unicode__(self):
        return self.item
	


