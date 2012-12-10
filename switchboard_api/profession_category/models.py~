from django.db import models
# list of health professions


class Profession_category(models.Model):
    # type of profession whether medicine or dental
    type_of_profession = models.CharField(max_length=50)
    # profession_name is a profession title
    # like Clinical Officer, AMO, ADO
    profession_name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s' % (self.profession_name)



