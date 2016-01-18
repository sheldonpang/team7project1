from django.conf.urls import patterns, include, url
from django.contrib import admin
from gps.views import locat,received,map

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', locat),
    url(r'^received/', received),
	url(r'^map/', map),
)
