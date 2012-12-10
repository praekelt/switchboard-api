from django.db import models
from switchboard_api.contact.models import Contact, Country


class Education(models.Model):
    # contact is a foreign key creates a
    # a relationship to table contact
    country = models.ForeignKey(Country, related_name='Education')
    contact = models.ForeignKey(Contact, related_name='Education') 
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
    level_of_course = models.CharField(max_length=20, choices=level_option)
    date_of_start = models.DateField()
    date_of_completion = models.DateField()
