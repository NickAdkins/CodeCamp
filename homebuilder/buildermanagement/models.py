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
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

class Room(models.Model):
    name = models.CharField(max_length = 200)
    project = models.ForeignKey('Project')
    sqfootage = models.IntegerField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Room, self).save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length = 200)
    contact_type = models.CharField(max_length = 2, choices=CONTACT_TYPES)
    group = models.ForeignKey(Group)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone1 = models.CharField(max_length = 12, blank=True, null=True)
    phone2 = models.CharField(max_length = 12, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Contact, self).save(*args, **kwargs)

class Item(models.Model):
    project = models.ForeignKey('Project')
    category = models.ForeignKey(Category)
    room = models.ManyToManyField(Room)
    material = models.CharField(max_length = 200)
    detail = models.TextField(max_length = 200)
    cost = models.IntegerField(default=0)
    picture = models.ImageField(upload_to ="images/%Y/%m/%d", blank=True, null=True)
    picture_url = models.URLField(max_length=200, blank=True, null=True)
    estimate_needed= models.BooleanField(default=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.material)
        return super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.material

class AddOn(models.Model):
    item = models.ForeignKey(Item)
    item_description = models.TextField(max_length = 200)
    cost = models.IntegerField(default=0)

    def __unicode__(self):
        return self.item_description

class Project(models.Model):
    name = models.CharField(max_length = 200)
    buyer = models.ForeignKey(Contact, related_name='buyer_set')
    plansfile = models.FileField('Plans file', upload_to="files/%Y/%m/%d", blank=True, null=True)
    builder = models.ForeignKey(Contact, related_name='builder_set')
    address = models.TextField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Phase(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    order_materials_by = models.DateTimeField(blank=True, null=True)
    depends_on = models.ForeignKey('self', blank=True, null=True)
    completed = models.BooleanField(default=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phase, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['start_date', 'completed']
