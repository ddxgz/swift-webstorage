from django.conf.urls import patterns, url
from disk.views import home, create_folder


urlpatterns = patterns(
    'disk.views',
    url(r'^$', home, name="home"), 
    url(r'^objects/(?P<prefix>(.+)+)?$', objectview,
    #     name="objectview"),

    # url(r'^login/$', login, name="login"),
    # url(r'^upload/(?P<container>.+?)/(?P<prefix>.+)?$', upload, name="upload"),
    url(r'^create_folder/(?P<prefix>.+)?$', create_folder, name="create_folder"),
#     url(r'^download/(?P<container>.+?)/(?P<objectname>.+?)$', download,
#         name="download"),
#     url(r'^delete/(?P<container>.+?)/(?P<objectname>.+?)$', delete_object,
#         name="delete_object"),
)
