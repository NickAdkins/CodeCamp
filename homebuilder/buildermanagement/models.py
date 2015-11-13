from django.db import models

# Create your models here.
class Project(models.Model):
    buyer = models.ForeignKey(Contact)

class Phase(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    order_by = models.DateTimeField()
    contact = ForeignKey(Contact)
    depends_on = ForeignKey('Phase', blank=True, null=True)

    def __unicode__(self):
        return self.name
