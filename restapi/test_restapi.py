import mock
import random

import unittest
from django.core.urlresolvers import reverse

import swiftclient
import restapi import HomeListener


class RESTApiTest(unittest.TestCase):
    """ Unit tests for swiftbrowser

    All calls using python-swiftclient.clients are replaced using mock """

    def test_get(self):
        swiftclient.client.get_account = mock.Mock(
            return_value=[{}, []],
            side_effect=swiftclient.client.ClientException(''))

        resp = self.client.get(reverse('containerview'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp['Location'],
                         'http://testserver' + reverse('login'))

        swiftclient.client.get_account = mock.Mock(return_value=[{}, []])

        resp = self.client.get(reverse('containerview'))
        self.assertEqual(resp.context['containers'], [])