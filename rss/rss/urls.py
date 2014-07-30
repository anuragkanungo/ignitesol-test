from django.conf.urls import patterns, include, url
from reader.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^input_feed/', input_feed),
    url(r'^input_form/', input_form),
    url(r'^output/', output),
)
