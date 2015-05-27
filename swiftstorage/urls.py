from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swiftstorage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'webadmin.views.index', name='index')
    # url(r'^container/', include('swiftbrowser.urls')),
    url(r'^', include('swiftbrowser.urls')),
    url(r'^videoplayer/', include('videoplayer.urls')),
)
