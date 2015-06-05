""" Standalone webinterface for Openstack Swift. """
# -*- coding: utf-8 -*-
import time
import urlparse
import hmac
import string
import random
from hashlib import sha1

from swiftclient import client

from django.conf import settings

import logging

logging.basicConfig(format='===========My:%(levelname)s:%(message)s', 
    level=logging.DEBUG)

def get_base_url(request):
    base_url = getattr(settings, 'BASE_URL', None)
    if base_url:
        return base_url
    if request.is_secure():
        base_url = "https://%s" % request.get_host()
    else:
        base_url = "http://%s" % request.get_host()
    return base_url


def replace_hyphens(olddict):
    """ Replaces all hyphens in dict keys with an underscore.

    Needed in Django templates to get a value from a dict by key name. """
    newdict = {}
    for key, value in olddict.items():
        key = key.replace('-', '_')
        newdict[key] = value
    return newdict


def prefix_list(prefix):
    prefixes = []

    if prefix:
        elements = prefix.split('/')
        elements = filter(None, elements)
        prefix = ""
        for element in elements:
            prefix += element + '/'
            prefixes.append({'display_name': element, 'full_name': prefix})

    return prefixes


def pseudofolder_object_list(objects, prefix):
    pseudofolders = []
    objs = []

    duplist = []

    for obj in objects:
        # Rackspace Cloudfiles uses application/directory
        # Cyberduck uses application/x-directory
        if obj.get('content_type', None) in ('application/directory',
                                             'application/x-directory'):
            obj['subdir'] = obj['name']

        if 'subdir' in obj:
            # make sure that there is a single slash at the end
            # Cyberduck appends a slash to the name of a pseudofolder
            entry = obj['subdir'].strip('/') + '/'
            if entry != prefix and entry not in duplist:
                duplist.append(entry)
                pseudofolders.append((entry, obj['subdir']))
        else:
            objs.append(obj)

    return (pseudofolders, objs)


def get_temp_key(storage_url, auth_token):
    """ Tries to get meta-temp-url key from account.
    If not set, generate tempurl and save it to acocunt.
    This requires at least account owner rights. """

    logging.debug('  in get_temp_key:  '  )

    try:
        account = client.head_account(storage_url, auth_token)
    except client.ClientException:
        return None
    logging.debug(' account in get_temp_key: %s ' % account)

    key = account.get('x-account-meta-temp-url-key')
    logging.debug(' key in get_temp_key: %s ' % key)

    if not key:
        chars = string.ascii_lowercase + string.digits
        key = ''.join(random.choice(chars) for x in range(32))
        headers = {'x-account-meta-temp-url-key': key}
        try:
            client.post_account(storage_url, auth_token, headers)
        except client.ClientException:
            return None
    return key


def get_temp_url(storage_url, auth_token, container, objectname, expires=600):
    key = get_temp_key(storage_url, auth_token)
    logging.debug(' storage_url in get_temp_url: %s ' % storage_url)
    if not key:
        return None

    expires += int(time.time())
    url_parts = urlparse.urlparse(storage_url)
    logging.debug(' ----- stop here url_parts:%s ' % url_parts.path)

    path = "%s/%s/%s" % (url_parts.path, container, objectname)
    base = "%s://%s" % (url_parts.scheme, url_parts.netloc)
    hmac_body = 'GET\n%s\n%s' % (expires, path)

    logging.debug(' ----- stop here path:%s , base:%s, hmac_body:%s' % (
        path,base,hmac_body))

    sig = hmac.new(key, hmac_body, sha1).hexdigest()
    logging.debug('lourl: %s%s?temp_url_sig=%s&temp_url_expires=%s' % (
        base, path, sig, expires))
    url_ = ("%s%s?temp_url_sig=%s&temp_url_expires=%s" % (
        base, path, sig, expires))
    logging.debug('url: %s' % url_)
    return str(url_)


# storage_url, auth_token = client.get_auth(
#                                     'http://10.200.46.211:8080/auth/v1.0',
#                                     'test:tester',
#                                   'testing',
#                                   auth_version=1)
#             # logging.debug('rs: %s'% swiftclient.client.get_auth(
#             #                         self.conf.auth_url,
#             #                         self.conf.account_username,
#             #                       self.conf.password,
#             #                       auth_version=1))
# logging.debug('url:%s, toekn:%s' % (storage_url, auth_token))
         
# temp_url = get_temp_url(storage_url, auth_token,
#                                           'disk', 'fold1/fqrouter2.12.7.apk')
# print(temp_url)