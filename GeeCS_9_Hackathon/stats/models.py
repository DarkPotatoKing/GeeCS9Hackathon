from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  Subject(models.Model):
    rank = models.IntegerField(default=0)
    slots = models.IntegerField(default=0)
    demand = models.IntegerField(default=0)
    subject = models.CharField(max_length=50, default="subj")
    section = models.CharField(max_length=20, default="section")
    prof = models.CharField(max_length=100,  default="prof")
    sched = models.CharField(max_length=1000, default="sched")
    units = models.IntegerField(default=3)

    def __str__(self):
        return 'Rank {} {} {} {}/{} {} {} {}'.format(self.rank, self.subject, self.section, self.demand, self.slots, self.units,  self.prof, self.sched)
