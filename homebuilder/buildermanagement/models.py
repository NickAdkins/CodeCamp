from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime

# Create your models here.

CONTACT_TYPES = (
                    ('sc', 'Subcontractor'),
                    ('hb', 'Home Builder'),
                    ('b', 'Buyer'),
                    ('v', 'Vendor'),
                )

class Group(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Group, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length = 200)
    project = models.ForeignKey('Project')

    def __unicode__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length = 200)
    project = models.ForeignKey('Project')
    sqfootage = models.IntegerField()

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    contact_type = models.CharField(max_length = 2, choices=CONTACT_TYPES)
    group = models.ForeignKey(Group, blank=True, null=True)
    name = models.CharField(max_length = 200)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone1 = models.CharField(max_length = 12, blank=True, null=True)
    phone2 = models.CharField(max_length = 12, blank=True, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    project = models.ForeignKey('Project')
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
    cost = models.IntegerField(default=0)

    def __unicode__(self):
        return self.item_description

class Project(models.Model):
    buyer = models.ForeignKey(Contact)
    name = models.CharField(max_length = 200)
    buyer = models.ForeignKey(Contact, related_name='buyer_set')
    plansfile = models.FileField(upload_to="files/%Y/%m/%d", blank=True, null=True)
    builder = models.ForeignKey(Contact, related_name='builder_set')
    address = models.TextField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

class Phase(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    order_by = models.DateTimeField()
    contact = models.ForeignKey(Contact)
    depends_on = models.ForeignKey('Phase', blank=True, null=True)

    def __unicode__(self):
        return self.name
