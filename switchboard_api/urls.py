from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from doctor import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'switchboard_api.views.home', name='home'),
    # url(r'^switchboard_api/', include('switchboard_api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^add/$', 'doctor.views.add', name='add'),
)

