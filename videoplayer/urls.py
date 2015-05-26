from django.conf.urls import patterns, url
from videoplayer.views import videoplayer
from swiftbrowser.views import containerview, objectview, download,\
    delete_object, login, tempurl, upload, create_pseudofolder,\
    create_container, delete_container, public_objectview, toggle_public,\
    edit_acl

urlpatterns = patterns(
    # 'swiftbrowser.views',
    # url(r'^$', index, name="index"), 

    url(r'^(?P<container>.+?)/(?P<objectname>.+?)$', videoplayer,
        name="videoplayer"),

)
