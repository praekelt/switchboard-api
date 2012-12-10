from django.contrib import admin

from switchboard_api.facility.models import Facility, District, FacilityType

admin.site.register(Facility)
admin.site.register(District)
admin.site.register(FacilityType)

