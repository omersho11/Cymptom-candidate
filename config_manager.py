import configparser
import os


class ConfigManager(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.path = os.path.join(os.path.expanduser('~'), '.aws\\credentials')
        self.config.read(self.path)

    def get_creds(self):
        aws_access_key_id = self.config.get('default', 'aws_access_key_id')
        aws_secret_access_key = self.config.get('default', 'aws_secret_access_key')
        return {"aws_access_key_id": aws_access_key_id, "aws_secret_access_key": aws_secret_access_key}