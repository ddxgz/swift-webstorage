from __future__ import absolute_import, division, print_function

from wsgiref import simple_server
import falcon
import json
import Queue
import sys, os
import logging

import swiftclient

from config import Config

logging.basicConfig(format='===========%(levelname)s:%(message)s=========', 
    level=logging.DEBUG)
#sys.path.append('.')

class HomeListener:
    def __init__(self):
        self.conf = Config('swiftconf.conf')
    def on_get(self, req, resp):
        try:
            username = req.get_header('username') or 'un'
            password = req.get_header('password') or 'pw'
            logging.debug('username:%s, password:%s' % (username, password))
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'when read from req, please check if the req is correct.')
        try:
            logging.debug('self.conf.auth_url: %s,   conf.auth_version: %s' % (
                self.conf.auth_url, self.conf.auth_version))
            conn = swiftclient.Connection(self.conf.auth_url,
                                  'test:tester',
                                  'testing',
                                  auth_version=self.conf.auth_version or 1)
            meta, objects = conn.get_container(self.conf.container)
            logging.debug('meta: %s,   objects: %s' % (meta, objects))
            resp_dict = {}
            resp_dict['meta'] = meta
            logging.debug('resp_dict:%s' % resp_dict)
            objs = {}
            for obj in objects:
                logging.debug('obj:%s' % obj.get('name'))
                objs[obj.get('name')] = obj
            resp_dict['objects'] = objs
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'username or password not correct!')
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(resp_dict, encoding='utf-8', sort_keys=True, indent=4)


    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
            logging.debug('req:%s' % raw_json)
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'when read from req, please check if the req is correct.')
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
            logging.debug('result json:%s' % result_json)
            logging.info('start to run process....')
            # self.queue.put(result_json)
        except:
            raise falcon.HTTPError(falcon.HTTP_400, 'malformed json')
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')

    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass



app = falcon.API()

# things = ThingsRe()
home_listener = HomeListener()

# app.add_route('/things', things)
app.add_route('/v1/disk', home_listener)


# Useful for debugging problems in your API; works with pdb.set_trace()
# if __name__ == '__main__':
#     httpd = simple_server.make_server('127.0.0.1', 8008, app)
#     httpd.serve_forever()

# conf = Config('swiftconf.conf')
# conn = swiftclient.Connection(conf.auth_url,
#                                   'test:tester',
#                                   'testing',
#                                   auth_version=conf.auth_version or 1)
# conn.head_account()