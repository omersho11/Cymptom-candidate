import configparser
from constants import CREDS_FILE_PATH


class ConfigManager(object):
    def __init__(self, creds_file_path=CREDS_FILE_PATH):
        self.config = configparser.ConfigParser()
        self.path = creds_file_path
        self.config.read(self.path)

    def get_creds(self):
        aws_access_key_id = self.config.get('default', 'aws_access_key_id')
        aws_secret_access_key = self.config.get('default', 'aws_secret_access_key')
        return {"aws_access_key_id": aws_access_key_id, "aws_secret_access_key": aws_secret_access_key}
