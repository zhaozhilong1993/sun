from django.conf.urls import patterns, include, url

from django.contrib import admin

from earth.views import *

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # web index
    url(r'^sun/index/$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),

    # web blog
    url(r'^blog/$', blog, name='blog'),

    # web agent
    url(r'^agent/$', agent, name='agent'),

    # web contact
    url(r'^contact/$', contact, name='contact'),
)
