from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class country(models.Model):
    name = models.CharField(max_length=60,unique=True, primary_key=True)
    
class contact(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=40)

    gender_option = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_option)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=30,null=True)
    postal_address = models.CharField(max_length=100,null=True)
    vodacom_phone = models.IntegerField(null=True)
    other_phone = models.IntegerField(null=True)
    email_address = models.EmailField(null=True)
class facility(models.Model):
    name_of_facility=models.CharField(max_length=100)
    facility_option = (
            ('Ministry of Health','Ministry of Health'),
            ('Region', 'Region'),
            ('District', 'District'),
            ('Training Institution', 'Training Institution'),
            ('Hospital', 'Hospital'),
            ('Health Centre', 'Health Centre'),
            ('Dispensary', 'Dispensary'),)
        
    type_of_facility = models.CharField(max_length=50,choices=facility_option)
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    postal_address = models.CharField(max_length=50,null=True)
    email_address = models.EmailField(null=True)
    telephone_number = models.CharField(max_length=20, null=True)
class job_description(models.Model):
    facility_id = models.ForeignKey(facility)
    contact_id = models.ForeignKey(contact) 
    duty_post = models.CharField(max_length=50)
    appointed_title = models.CharField(max_length=50)
    terms_option = (
            ('Permanent','Permanent'),
            ('Contract', 'Contract'),
            ('Volunteer', 'Volunteer'),
            ('Temporary', 'Temporary'),)
    terms_of_employment = models.CharField(max_length=20,choices=terms_option)
    date_updated = models.DateField( )
class education_history(models.Model):
    contact_id = models.ForeignKey(contact) 
    college_attended = models.CharField(max_length=50)
    college_location = models.CharField(max_length=40)
    name_of_course = models.CharField(max_length=50)
    level_option = (
            ('Certificate','Certificate'),
            ('Diploma', 'Diploma'),
            ('Advanced Diploma', 'Advanced Diploma'),
            ('Bachelor', 'Bachelor'),
            ('Master', 'Master'),
            ('PhD', 'PhD'),
            )
    level_of_course = models.CharField(max_length=20,choices=level_option)
    date_of_start = models.DateField( )
    date_of_completion = models.DateField( )
class application(models.Model):
    application_option = (
            ('Basic','Basic'),
            ('Additional', 'Additional'),
            ('Renew', 'Renew'),
            )
    application_type = models.CharField(max_length=10, choices=application_option)
    application_name = models.CharField(max_length=100)
    date_of_application = models.DateField( )
    application_approval = models.CharField(max_length=20)
    date_of_approval = models.DateField( )
    approval_remarks = models.CharField(max_length=100)
    contact_id = models.ForeignKey(contact)
class payment(models.Model):
    pay_option = (
            ('Cash','Cash'),
            ('Cheque', 'Cheque'),
            ('Pay in slip', 'Pay in slip'),
            )
     
    payment_type = models.CharField(max_length=20, choices=pay_option)
    
    apps_option = (
            ('Full Registration','Full Registration'),
            ('Provisional Registration', 'Provisional Registration'),
            ('Inteship Registration', 'Inteship Registration'),
            )
    application_category = models.CharField(max_length=30, choices=apps_option)
    
    currency_option = (
            ('USA Dollar','USA Dollar'),
            ('Tanzanian Shillings', 'Tanzanian Shillings'),
            )
    type_of_currency = models.CharField(max_length=30, choices=currency_option)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2)
    date_of_payment = models.DateField( )
    application_id = models.ForeignKey(application)
class certification(models.Model):
    payment_id = models.ForeignKey(payment)
    contact_id = models.ForeignKey(contact)
    cert_option = (
            ('New','New'),
            ('Old', 'Old'),
            )
    certification_category = models.CharField(max_length=10, choices=cert_option)
    registration_number = models.CharField(max_length=30)
    date_of_issue = models.DateField( )
    date_of_expiry = models.DateField( )
    application_id = models.ForeignKey(application)
    
class profession_category(models.Model):
    profe_option = (
            ('Medicine','Medicine'),
            ('Dental', 'Dental'),
            )
    type_of_profession = models.CharField(max_length=15, choices=profe_option)
    profession = models.CharField(max_length=40)
class registered_profession(models.Model):
    profession_id = models.ForeignKey(profession_category)
    registration_number = models.ForeignKey(certification)
    date_of_registration = models.DateField( )
class payrol(models.Model):
    check_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=60)
    date_of_birth = models.DateField( )    
    profession = models.CharField(max_length=60)   
                
