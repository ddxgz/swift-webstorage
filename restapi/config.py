import os

from six.moves import configparser


class Config(object):
    def __init__(self, conf_file=None):
        if conf_file:
            self.config_file = conf_file
            self._get_config(specified=True)
        else:
            self._get_config()

    def _get_config(self, specified=False):
        if specified is True:
            config_file = self.config_file
        else:
            config_file = os.environ.get('SWIFTCLIENT_CONFIG_FILE',
                                     './swiftclient.conf')
        config = configparser.SafeConfigParser({'auth_version': '1'})
        config.read(config_file)
        if config.has_section('swiftconf'):
            auth_host = config.get('swiftconf', 'auth_host')
            auth_port = config.getint('swiftconf', 'auth_port')
            auth_ssl = config.getboolean('swiftconf', 'auth_ssl')
            auth_prefix = config.get('swiftconf', 'auth_prefix')
            self.auth_version = config.get('swiftconf', 'auth_version')
            self.account = config.get('swiftconf', 'account')
            self.username = config.get('swiftconf', 'username')
            self.password = config.get('swiftconf', 'password')
            self.auth_url = ""
            if auth_ssl:
                self.auth_url += "https://"
            else:
                self.auth_url += "http://"
            self.auth_url += "%s:%s%s" % (auth_host, auth_port, auth_prefix)
            if self.auth_version == "1":
                self.auth_url += 'v1.0'
            self.account_username = "%s:%s" % (self.account, self.username)
        else:
            self.skip_tests = True
        if config.has_section('catchconf'):
            self.container = config.get('catchconf', 'container')
            self.video_dir = config.get('catchconf', 'video_dir')
            self.shell_dir = config.get('catchconf', 'shell_dir')
            self.upload_file = config.get('catchconf', 'upload_file')
            uploading_interval = config.get('catchconf',
                                                 'uploading_interval')
            loopcount = config.get('catchconf', 'loopcount')
            threshold_container = config.get('catchconf',
                                                  'threshold_container')
            self.uploading_interval = int(uploading_interval)
            self.loopcount = int(loopcount)
            self.threshold_container = int(threshold_container)
            self.upload_dir = config.get('catchconf', 'upload_dir')
            wait_for_video_sec = config.get('catchconf',
                                                  'wait_for_video_sec')
            self.wait_for_video_sec = int(wait_for_video_sec)

        if config.has_section('devsetting'):
            no_catch = config.get('devsetting', 'no_catch')
            if no_catch is '0':
                self.no_catch = 0
            else:
                self.no_catch = 1
            auto_rename = config.get('devsetting', 'auto_rename')
            if auto_rename is '0':
                self.auto_rename = 0
            else:
                self.auto_rename = 1
