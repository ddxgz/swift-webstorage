# -*- coding: utf-8 -*-
import time
import urlparse
import hmac
import string
import random
from hashlib import sha1

from swiftclient import client

import logging

logging.basicConfig(format='===========My:%(levelname)s:%(message)s', 
    level=logging.DEBUG)


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


def get_fine_grained_temp_key(storage_url, auth_token, container_name=None):
    """ Tries to get meta-temp-url key from account.
    If not set, generate tempurl and save it to acocunt.
    This requires at least account owner rights. """

    logging.debug('  in get_fine_grained_temp_key: container_name:%s, \
        storage_url:%s ' % 
        (container_name, storage_url) )

    try:
        if container_name:
            container = client.head_container(storage_url, auth_token, 
                container_name)
            key = container.get('x-container-meta-temp-url-key')
            logging.debug(' key in get_fine_grained_temp_key container: %s ' % key)
        else:
            account = client.head_account(storage_url, auth_token)
            key = account.get('x-account-meta-temp-url-key')
            logging.debug(' key in get_fine_grained_temp_key account: %s ' % key)
    except client.ClientException:
        return None
    # logging.debug(' account or container in get_temp_key: %s ' 
    #     % account or container)

    if not key:
        chars = string.ascii_lowercase + string.digits
        key = ''.join(random.choice(chars) for x in range(32))
        if container_name:
            headers = {'x-container-meta-temp-url-key': key}
            try:
                client.post_container(storage_url, auth_token, container_name, 
                    headers)
                logging.debug(' post_container')

            except client.ClientException:
                return None
            raise ValueError('cannot get key, have no account rights to \
                get account key!')
        else:
            
            headers = {'x-account-meta-temp-url-key': key}
            try:
                client.post_account(storage_url, auth_token, headers)
                logging.debug(' post_account')

            except client.ClientException:
                return None
    return key


def get_temp_url(storage_url, auth_token, container, objectname, expires=6000):
    # key = get_temp_key(storage_url, auth_token)
    key = get_fine_temp_key(storage_url, auth_token)
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


storage_url, auth_token = client.get_auth(
                                    'http://10.200.46.211:8080/auth/v1.0',
                                    'test:tester',
                                  'testing',
                                  auth_version=1)
            # logging.debug('rs: %s'% swiftclient.client.get_auth(
            #                         self.conf.auth_url,
            #                         self.conf.account_username,
            #                       self.conf.password,
            #                       auth_version=1))
logging.debug('url:%s, toekn:%s' % (storage_url, auth_token))
         
temp_url = get_fine_grained_temp_key(storage_url, auth_token,
                                          'disk')
print(temp_url)