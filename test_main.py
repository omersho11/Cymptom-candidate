from unittest import TestCase
from ec2_client import EC2Client
from constants import DEFAULT_REGION, DEFAULT_FILE_PATH


class TestClass(TestCase):

    def test_get_data_from_region(self, region=DEFAULT_REGION):
        """
        Tests if the client can obtain information from a region
        :param region: any available EC2 region, by default it's us-east-2
        """
        client = EC2Client()

        assert client.get_data_from_region(region) is not None

        del client

    def test_get_data_from_all_regions(self):
        """
        Tests if the client can obtain information from all amazon EC2 regions
        """
        client = EC2Client()

        assert client.get_data_from_all_regions()

        del client

    def test_write_data_to_file(self, file_path=DEFAULT_FILE_PATH):
        """
        Tests if data can be written to a file
        :param file_path: path of the wanted output file, by default it's the cwd
        """
        client = EC2Client()
        assert client.write_to_file(file_path)

        with open(file_path, 'r') as f:
            file_content = f.read()

        assert file_content

        del client
