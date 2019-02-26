from django.contrib import admin
from django.conf.urls import url

from earth.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # web index
    url(r'^sun/index/$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),

]