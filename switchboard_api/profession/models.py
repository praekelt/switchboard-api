from django.db import models
from switchboard_api.profession_category.models import Profession_category
from switchboard_api.contact.models import Contact


class Profession(models.Model):
    # contact is a foreign key from contact of a doctor
    contact = models.ForeignKey(Contact, related_name='Profession')
    # profession category is a foreign key from profession category
    profession_category = models.ForeignKey(Profession_category,
                                          related_name='Profession')
    # specialization of a doctor in that profession category
    specialization = models.CharField(max_length=50)
    # date of data entry
    date = models.DateField()
    
    def __unicode__(self):
        return u'%s' % (self.profession_name)




