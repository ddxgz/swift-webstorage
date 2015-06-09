import sys
import os
import ast
import urllib2
import requests

import logging

logging.basicConfig(format='===========%(levelname)s:%(message)s=========', 
    level=logging.DEBUG)


class Visit():
	def __init__(self, baseurl):
		self.baseurl = baseurl

	def get(self, suffix_url='', headers=None, data=None):
		req = urllib2.Request(self.baseurl+suffix_url, headers=headers, 
			data=data)
		resp = urllib2.urlopen(req)
		page = resp.read()
		logging.debug('resp:%s, page:%s' % (resp, page))

	def put(self, suffix_url='', headers=None, data=None):
		req = urllib2.Request(self.baseurl+suffix_url, headers=headers, 
			data=data)
		req.get_method = lambda: 'PUT'
		resp = urllib2.urlopen(req)
		page = resp.read()
		logging.debug('resp:%s, page:%s' % (resp, page))
		return page

	def put_file(self, filename='', suffix_url='', headers=None, data=None):
		resp_str = self.put(suffix_url=suffix_url, headers=headers)
		resp = ast.literal_eval(resp_str)
		logging.debug('resp:%s' % (resp))
		token = resp.get('auth_token')
		storage_url = resp.get('storage_url')
		headers = {'x-storage-token':token}
		files = {'file': open(filename)}
		put_resp = requests.put(storage_url, files=files, headers=headers)
		logging.debug('put_resp:%s' % (put_resp))

	def delete(self, suffix_url='', headers=None, data=None):
		req = urllib2.Request(self.baseurl+suffix_url, headers=headers, 
			data=data)
		req.get_method = lambda: 'DELETE'
		resp = urllib2.urlopen(req)
		page = resp.read()
		logging.debug('resp:%s, page:%s' % (resp, page))
		return page


headers = { 'username':'test:tester',
			'password':'testing' }
visit = Visit('http://10.200.44.84:8080/v1/disk')
# visit.get(headers=headers)
# visit.put(suffix_url='/curl.py', headers=headers)
# visit.put_file(filename='curl.py', suffix_url='/fold3/curl.py', headers=headers)
# visit.delete(suffix_url='/fold3/curl.py', headers=headers)
