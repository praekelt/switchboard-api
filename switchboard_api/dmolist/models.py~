from django.db import models


class Dmolist(models.Model):
    # full name of a doctor
    first_name = models.CharField(max_length=40)
    # last name of a doctor
    middle_name = models.CharField(max_length=40)
    # last name of a doctor
    last_name = models.CharField(max_length=40)
    # profession of a doctor like AMO, CO
    profession_name = models.CharField(max_length=60)
    # working district of a doctor
    facility = models.CharField(max_length=50, null=True)
    # working district of a doctor
    district = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)
