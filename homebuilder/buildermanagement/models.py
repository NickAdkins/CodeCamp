from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length = 200)
    project = models.ForeignKey(Project)
    sqfootage = models.IntegerField()

    def __unicode__(self):
        return self.name

class Item(models.Model):
    project = models.ForeignKey(Project)
    category = models.ForeignKey(Category)
    room = models.ManyToManyField(Room)
    material = models.CharField(max_length = 200)
    detail = models.TextField(max_length = 200)
    cost = models.IntegerField()
    picture = models.ImageField(upload_to ="images/%Y/%m/%d", blank=True, null=True)
    picture_url = models.URLField(max_length = 200, blank=True, null=True)
    estimate_needed= models.BooleanField(default=False)

    def __unicode__(self):
        return self.material

class AddOn(models.Model):
    item = models.ForeignKey(Item)
    item_description = models.TextField(max_length = 200)
    cost = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.item_description
