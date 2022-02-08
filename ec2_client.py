import boto3
from config_manager import ConfigManager
from botocore.exceptions import ClientError
from information_manager import InstancesInformation
from constants import DEFAULT_REGION


class EC2Client(object):
    """
    Class wrapper for the boto3 client, allows for easier interaction and api calls
    """
    def __init__(self, default_region: str = DEFAULT_REGION):
        self.creds = ConfigManager().get_creds()  # Obtaining Creds
        self.default_region: str = default_region  # default region is us-east-2

        self.ec2 = boto3.client("ec2", region_name=default_region)
        self.regions = [region['RegionName'] for region in self.ec2.describe_regions()['Regions']]
        del self.ec2
        # Creating a boto3 client to obtain a list of all regions available, then deleting.

    def get_data_from_region(self, region: str):
        """
        Allows to obtain a formatted data of a singular instance
        :param region: string: one of possible regions,
        :return: InstanceInformation object containing all requested information about evert instance from specified
        region
        """
        data = {}
        try:
            ec2 = boto3.client("ec2",
                               region_name=region,
                               aws_access_key_id=self.creds['aws_access_key_id'],
                               aws_secret_access_key=self.creds['aws_secret_access_key'])
            data = ec2.describe_instances()
        except ClientError:
            print(f'{region}: No instances found')
            # filtering out UnauthorizedOperation errors since I don't have access to every instance
            # can be substituted for log module
        if data:
            print(f'{region}: instances found')  # can be substituted for log module
            output = InstancesInformation(information_dictionary=data)
            return output
        return None

    def get_data_from_all_regions(self) -> dict:
        """
        Collects the information about all machines from different regions and
        compiles it to a single dictionary
        :return: dictionary where d[region] = formatted data of all machines
        """
        data = {}
        for region in self.regions:
            data[region] = self.get_data_from_region(region)
        return data

    def write_to_file(self, file):
        with open(file, 'w') as f:
            f.write(str(self.get_data_from_all_regions()))
            return True
