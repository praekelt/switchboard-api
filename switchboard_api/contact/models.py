from django.db import models

# Create your models here.
class country(models.Model):
    country_name=models.CharField(max_length=40)
    
    def __unicode__(self):
	return u'%s' % (self.country_name)

class contact(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    nationality = models.ForeignKey('country', related_name='contact')
    postal_address = models.CharField(max_length=70,null=True)
    vodacom_phone = models.CharField(max_length=30,null=True)
    other_phone = models.CharField(max_length=30,null=True)
    email_address = models.EmailField(null=True)

    def __unicode__(self):
	return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)

