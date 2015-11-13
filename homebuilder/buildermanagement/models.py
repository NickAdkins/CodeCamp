from django.db import models
from django.contrib.auth.models import User


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

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    contact_type = models.CharField(max_length = 2, choices=CONTACT_TYPES)
    group = models.ForeignKey(Group)
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    address = models.TextField()
    phone1 = models.CharField(max_length = 12, blank=True, null=True)
    phone2 = models.CharField(max_length = 12, blank=True, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length = 200)
    buyer = models.ForeignKey(Contact)
    user = models.ForeignKey(User)
    plansfile = models.FileUploadField(upload_to="files/%Y/%m/%d", blank=True, null=True)
    builder = models.ForeignKey(Contact)
    address = models.TextField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
