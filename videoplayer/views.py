
# -*- coding: utf-8 -*-
import os
import logging
import time
import urlparse
import urllib2
import urllib
import requests
import hmac
from hashlib import sha1

from swiftclient import client

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.shortcuts import render

import swiftbrowser

logging.basicConfig(level=logging.DEBUG)


def videoplayer(request, container, objectname):
    """ Playing a video for a given container object """

    storage_url = request.session.get('storage_url', '')
    auth_token = request.session.get('auth_token', '')
    url = swiftbrowser.utils.get_temp_url(storage_url, auth_token,
                                          container, objectname)
    logging.debug('con:%s, obj:%s, videoplayer- storage_url:%s, auth_token:%s, url:%s' % 
        (container, objectname, storage_url, auth_token, url))
    if not url:
        logging.debug('no url:%s' % url)

    videofile = 'static/videos/'+objectname
    # LOCAL_VIDEO = '/static/videos/DEMO_1432693581.36215.mp4'
    urllib.urlretrieve (url, videofile)
    context = {'videofile': '/'+videofile}
    return render(request, 'videoplayer.html', context)