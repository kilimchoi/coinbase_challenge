from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r"^$", 'btcconverter.views.index'),
    (r"^index$", 'btcconverter.views.index'),
    # Examples:
    # url(r'^$', 'btcconverter.views.home', name='home'),
    # url(r'^btcconverter/', include('btcconverter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
