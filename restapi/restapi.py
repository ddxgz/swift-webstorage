from __future__ import absolute_import, division, print_function

from wsgiref import simple_server
import falcon
import json
import Queue
import sys, os
import logging

from utils import get_temp_key, get_base_url, get_temp_url

import swiftclient
# from swiftclient import client

from config import Config

logging.basicConfig(format='===========My:%(levelname)s:%(message)s=========', 
    level=logging.DEBUG)
#sys.path.append('.')


class PathListener:
    def __init__(self):
        self.conf = Config('swiftconf.conf')

    def on_get(self, req, resp, path, thefile):
        """
        :param req.header.username: the username, should be tenant:user when dev
        :param req.header.password: password 

        :returns: a json contains all objects in disk container, and metameata
                {"meta":{}, "objects":{"obj1": {}}}
        """
        try:
            username = req.get_header('username') or 'un'
            password = req.get_header('password') or 'pw'
            logging.debug('username:%s, password:%s' % (username, password))
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'when read from req, please check if the req is correct.')
        try:
            # if path2file:
            logging.debug('path2file:%s, file:%s' % (path, thefile))
            # logging.debug('self.conf.auth_url: %s,  conf.auth_version: %s' % (
            #     self.conf.auth_url, self.conf.auth_version))
            # conn = swiftclient.Connection(self.conf.auth_url,
            #                       self.conf.account_username,
            #                       self.conf.password,
            #                       auth_version=self.conf.auth_version or 1)
            # meta, objects = conn.get_container(self.conf.container)
            # meta, obj = conn.get_object(self.conf.container, path2file)
            # logging.debug('meta: %s,   obj: %s' % (meta, obj))

            storage_url, auth_token = swiftclient.client.get_auth(
                                    self.conf.auth_url,
                                    self.conf.account_username,
                                  self.conf.password,
                                  auth_version=1)
            # logging.debug('rs: %s'% swiftclient.client.get_auth(
            #                         self.conf.auth_url,
            #                         self.conf.account_username,
            #                       self.conf.password,
            #                       auth_version=1))
            logging.debug('url:%s, toekn:%s' % (storage_url, auth_token))
         
            temp_url = get_temp_url(storage_url, auth_token,
                                          self.conf.container, path2file)
            resp_dict = {}
            # resp_dict['meta'] = meta
            # objs = {}
            # for obj in objects:
            #     logging.debug('obj:%s' % obj.get('name'))
            #     objs[obj.get('name')] = obj
            resp_dict['temp_url'] = temp_url
            logging.debug('resp_dict:%s' % resp_dict)

        except:
            raise falcon.HTTPBadRequest('bad req', 
                'username or password not correct!')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(resp_dict, encoding='utf-8', 
            sort_keys=True, indent=4)
        resp.body = temp_url
        # resp.stream = obj
        # resp.head = meta


class HomeListener:
    def __init__(self):
        self.conf = Config('swiftconf.conf')

    def on_get(self, req, resp):
        """
        :param req.header.username: the username, should be tenant:user when dev
        :param req.header.password: password 

        :returns: a json contains all objects in disk container, and metameata
                {"meta":{}, "objects":{"obj1": {}}}
        """
        try:
            username = req.get_header('username') or 'un'
            password = req.get_header('password') or 'pw'
            logging.debug('username:%s, password:%s' % (username, password))
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'when read from req, please check if the req is correct.')
        try:
            # if path2file:
            logging.debug('self.conf.auth_url: %s,  conf.auth_version: %s' % (
                self.conf.auth_url, self.conf.auth_version))
            conn = swiftclient.Connection(self.conf.auth_url,
                                  self.conf.account_username,
                                  self.conf.password,
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
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(resp_dict, encoding='utf-8', 
            sort_keys=True, indent=4)


    def on_post(self, req, resp):
        try:
            username = req.get_header('username') or 'un'
            password = req.get_header('password') or 'pw'
            logging.debug('username:%s, password:%s' % (username, password))
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'when read from req, please check if the req is correct.')
        try:
            # post_data = req.env
            logging.debug('env:%s , \nstream:%s, \ncontext:%s, \ninput:%s' % (
                req.env, req.stream.read(), req.context, req.env['wsgi.input'].read()))
            # logging.debug('self.conf.auth_url: %s,   conf.auth_version: %s' % (
            #     self.conf.auth_url, self.conf.auth_version))
            conn = swiftclient.Connection(self.conf.auth_url,
                                  self.conf.account_username,
                                  self.conf.password,
                                  auth_version=self.conf.auth_version or 1)
            conn.put_object('disk', 'testfile', req.stream, 
                chunk_size=65536)
            # meta, objects = conn.get_container(self.conf.container)
            # logging.debug('meta: %s,   objects: %s' % (meta, objects))
            # resp_dict = {}
            # resp_dict['meta'] = meta
            # logging.debug('resp_dict:%s' % resp_dict)
            # objs = {}
            # for obj in objects:
            #     logging.debug('obj:%s' % obj.get('name'))
            #     objs[obj.get('name')] = obj
            # resp_dict['objects'] = objs
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'username or password not correct!')
        # resp.status = falcon.HTTP_202
        # resp.body = json.dumps(resp_dict, encoding='utf-8', sort_keys=True, indent=4)


        resp.status = falcon.HTTP_202
        resp.body = json.dumps({}, encoding='utf-8')


    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass


class SinkAdapter(object):

    # engines = {
    #     'ddg': 'https://duckduckgo.com',
    #     'y': 'https://search.yahoo.com/search',
    # }
    conf = Config('swiftconf.conf')
    def __call__(self, req, resp, path2file):
        # url = self.engines[engine]
        # params = {'q': req.get_param('q', True)}
        # result = requests.get(url, params=params)
        logging.debug('in sink req:%s   path2file:%s' % (req,path2file))
        try:
            username = req.get_header('username') or 'un'
            password = req.get_header('password') or 'pw'
            logging.debug('username:%s, password:%s' % (username, password))
        except:
            raise falcon.HTTPBadRequest('bad req', 
                'when read from req, please check if the req is correct.')

        if req.method is 'GET' or 'get':
            try:
                storage_url, auth_token = swiftclient.client.get_auth(
                                        self.conf.auth_url,
                                        self.conf.account_username,
                                      self.conf.password,
                                      auth_version=1)
                # logging.debug('rs: %s'% swiftclient.client.get_auth(
                #                         self.conf.auth_url,
                #                         self.conf.account_username,
                #                       self.conf.password,
                #                       auth_version=1))
                logging.debug('url:%s, toekn:%s' % (storage_url, auth_token))
             
                temp_url = get_temp_url(storage_url, auth_token,
                                              self.conf.container, path2file)

                resp_dict = {}
                # resp_dict['meta'] = meta
                # objs = {}
                # for obj in objects:
                #     logging.debug('obj:%s' % obj.get('name'))
                #     objs[obj.get('name')] = obj
                resp_dict['temp_url'] = temp_url
                resp_dict['path2file'] = path2file
                # logging.debug('resp_dict:%s' % resp_dict)

            except:
                raise falcon.HTTPBadRequest('bad req', 
                    'username or password not correct!')
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(resp_dict, encoding='utf-8', 
            sort_keys=True, indent=4)
        # resp.body = temp_url


app = falcon.API()

# things = ThingsRe()
home_listener = HomeListener()
path_listener = PathListener()

# app.add_route('/things', things)
# app.add_route('/v1/disk/{path}/{file}', path_listener)
app.add_route('/v1/disk', home_listener)

sink = SinkAdapter()
app.add_sink(sink, r'^/v1/disk/(?P<path2file>.+?)$')

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