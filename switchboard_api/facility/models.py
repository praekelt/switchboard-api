from django.db import models
# Create your models here.


class District(models.Model):  
    # region name has more than one district
    region_name = models.CharField(max_length=50)
    # distric name is name of district facility found
    district_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.district_name)


class Facility_type(models.Model):
    # type of facility is like hospital,health centre,
    # dispersary,training institution,district,region
    type_of_facility = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % (self.type_of_facility)


class Facility(models.Model):
    # name of facility is the facility name
    name_of_facility = models.CharField(max_length=100)
    # type of facility is a foreign key creates 
    # a relationship with Facility_type
    type_of_facility = models.ForeignKey('Facility_type', related_name='facility')
    # owner is name of to whom facility belongs
    owner = models.CharField(max_length=20, null=True)
    # ownship type is like private, FBO, public
    ownship_type = models.CharField(max_length=20, null=True)
    # district is the foreign key from District
    district = models.ForeignKey('District', related_name='facility')
    # town where the facility found
    town = models.CharField(max_length=30)
    # postal address is the postal contact address
    postal_address = models.CharField(max_length=50, null=True)
    # email address of facility
    email_address = models.EmailField(null=True)
    # land line of the facility
    telephone_number = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return u'%s' % (self.name_of_facility
