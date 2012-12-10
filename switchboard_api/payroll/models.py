from django.db import models
# Create your models here.


class Payroll(models.Model):
    # full name of a doctor
    full_name = models.CharField(max_length=80)
    # last name of a doctor
    last_name = models.CharField(max_length=40)
    # check number of a doctor
    check_number = models.CharField(max_length=30)
    # date of birth of a doctor
    date_of_birth = models.DateField()
    # the current position of a doctor at facility
    designation = models.CharField(max_length=50, null=True)
    # working place (district) of a doctor
    district = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return u'%s' % (self.check_number)
