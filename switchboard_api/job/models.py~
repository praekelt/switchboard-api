from django.db import models
from contact.models import Contact
from facility.models import Facility
# job description of a doctor 


class Job_description(models.Model):
    # duty post is a designation of a doctor at facility
    duty_post = models.CharField(max_length=40)
    # appointed title is the title like head of section
    appointed_title = models.CharField(max_length=40)
    # date of data entry
    date = models.DateField()
    # contact_id is a foreign key creates a
    # a relationship to doctor's contact
    contact_id = models.ForeignKey(Contact, related_name='Job_description')
    # facility a foreign key creates a
    # a relationship to facility
    facility = models.ForeignKey(Facility, related_name='Job_description')
  
    def __unicode__(self):
        return  u'%s %s %s' % (self.duty_post,self.appointed_title,self.date)

