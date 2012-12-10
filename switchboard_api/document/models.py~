from django.db import models
from switchboard_api.contact.models import Contact
# documents of a doctor 


class Document(models.Model):
    # document name
    document_name = models.CharField(max_length=40)
    # application date is date of a day of submission
    submission_date = models.DateField()
    # contact is a foreign key creates a
    # a relationship to table contact
    contact = models.ForeignKey(Contact, related_name='Document')
  
    def __unicode__(self):
        return u'%s' % (self.document_name)

