from django.db import models
from switchboard_api.contact.models import Contact
# application of a doctor 


class Application(models.Model):
    # categories like basic, additional, renew
    application_category = models.CharField(max_length=40)
    # type of application
    # like full certificate, provisional, additional
    type_of_application = models.CharField(max_length=70)
    # status of application like pending, accepted, rejected 
    application_status = models.CharField(max_length=40)
    # application date is date of a day of application
    application_date = models.DateField()
    # contact is a foreign key creates a
    # a relationship to table contact
    contact = models.ForeignKey(Contact, related_name='Application')
  
    def __unicode__(self):
        return u'%s' % (self.type_of_application)

