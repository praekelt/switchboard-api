from tastypie.resources import ModelResource
from tastypie import fields
from contact.models import contact

class contactResource(ModelResource):
    
    class Meta:
        queryset = contact.objects.all()
        excludes = ['id']
        include_resource_uri = False


