from django.db import models
# list of countries for
# nationality of a doctor


class Country(models.Model):
    # name of country
    country_name = models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s' % (self.country_name)


class Contact(models.Model):
    # first name of a doctor is compulsory
    first_name = models.CharField(max_length=40)
    # middle name of a doctor is not compulsory
    middle_name = models.CharField(max_length=30, null=True)
    # last name of a doctor is compulsory
    last_name = models.CharField(max_length=40)
    # sex of a doctor is compulsory (male or female)
    gender = models.CharField(max_length=10)
    # date of birth of a doctor is compulsory
    date_of_birth = models.DateField()
    # nationality of a doctor is a born country.
    # it is selectable field, by default it is 'Tanzania'
    nationality = models.ForeignKey('Country', related_name='Contact')
    # postal address of a doctor can be null
    postal_address = models.CharField(max_length=70, null=True)
    # vodacom mobile number of a doctor can be null
    vodacom_phone = models.CharField(max_length=30, null=True)
    # other mobile number apart from vodacom number can be null
    other_phone = models.CharField(max_length=30, null=True)
    # email address of a doctor can be null
    email_address = models.EmailField(null=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.first_name,
                                self.middle_name, self.last_name)
