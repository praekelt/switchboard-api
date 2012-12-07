from django.db import models
from contact.models import Contact
# certification of a doctor 


class Certification(models.Model):
    # type of certification
    # like full certificate, provisional, additional
    type_of_certification = models.CharField(max_length=40)
    # registration number of a doctor is compulsory
    # will be used for verification for existence of doctor
    registration_number = models.CharField(max_length=40)
    # registration date is date of a day of licensing
    registration_date = models.DateField()
    # expiry date is date of a day of expiry of license
    expiry_date = models.DateField()
    # contact_id is a foreign key creates a
    # a relationship to table contact
    contact_id = models.ForeignKey(Contact, related_name='Certification')
  
    def __unicode__(self):
        return u'%s' % (self.registration_number)

