from django.db import models
from switchboard_api.contact.models import Contact
from switchboard_api.facility.models import Facility
# job description of a doctor 


class Job_description(models.Model):
    # duty post is the position at facility
    duty_post = models.CharField(max_length=50)
    # appointed title like head of section
    appointed_title = models.CharField(max_length=50)
    terms_option = (
            ('Permanent','Permanent'),
            ('Contract', 'Contract'),
            ('Volunteer', 'Volunteer'),
            ('Temporary', 'Temporary'),)
    terms_of_employment = models.CharField(max_length=20, choices=terms_option)
    # facility is a foreign key creates a
    # a relationship to table facility
    facility = models.ForeignKey(Facility, related_name='Job_description')
    # contact is a foreign key creates a
    # a relationship to table contact
    contact = models.ForeignKey(Contact, related_name='Job_description')
   

    def __unicode__(self):
        return u'%s' % (self.duty_post)


