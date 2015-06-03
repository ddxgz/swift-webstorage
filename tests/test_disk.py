#!/usr/bin/python
# -*- coding: utf8 -*-

import mock
import random

from django.test import TestCase
from django.core.urlresolvers import reverse

import swiftclient
import disk


class MockTest(TestCase):
    """ Unit tests for disk

    All calls using python-swiftclient.clients are replaced using mock """

    def test_diskview(self):
        swiftclient.client.get_container = mock.Mock(
            return_value=[{}, []],
            side_effect=swiftclient.client.ClientException(''))

        resp = self.client.get(reverse('disk', kwargs={}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp['Location'], 'http://testserver/')

        meta = {}
        objects = [{'subdir': 'pre'}, {'name': 'pre/fix'}]
        swiftclient.client.get_container = mock.Mock(
            return_value=(meta, objects))

        resp = self.client.get(reverse('disk', kwargs={}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['folders'], [('pre/', 'pre')])

        resp = self.client.get(reverse('disk',
                               kwargs={'prefix': 'pre/'}))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['folders'], [])
        self.assertEqual(resp.context['prefix'], 'pre/')

   