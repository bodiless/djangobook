from django.conf.urls import patterns, include, url

from django.contrib import admin

from mysite.views import *
from books.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^hour/(\d{1})/', one_hour_ahead),
    url(r'^datetime/', current_datetime),
    url(r'^for_loop/', for_loop),
    url(r'^if_cond/', if_cond),
	url(r'^if_equal/', if_equal),
    url(r'^get_meta/', get_meta),
    url(r'^search_form', search_form),
    url(r'^search', search),
)

