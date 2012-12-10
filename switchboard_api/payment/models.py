from django.db import models

# Create your models here.from django.db import models
from switchboard_api.contact.models import Contact
# documents of a doctor 


class Payment(models.Model):
    # type of payment
    type_of_payment = models.CharField(max_length=60)
    # type of currency
    type_of_currency = models.CharField(max_length=20)
    # amount
    amount = models.IntegerField(max_length=20)
    # payment date 
    date_of_payment = models.DateField()
    #status of payment
    payment_confirmation = models.CharField(max_length=40)
    # contact is a foreign key creates a
    # a relationship to table contact
    contact = models.ForeignKey(Contact, related_name='Payment')
  
    def __unicode__(self):
        return u'%s' % (self.type_of_payment)
