import boto3
from config_manager import ConfigManager
from botocore.exceptions import ClientError
from information_manager import InstancesInformation
from constants import DEFAULT_REGION


class EC2Client(object):
    """
    Class wrapper for the boto3 client, allows for easier interaction and api calls
    """
    def __init__(self, logger, default_region: str = DEFAULT_REGION):
        self.logger = logger
        self.creds = ConfigManager().get_creds()  # Obtaining Creds
        self.default_region: str = default_region  # default region is us-east-2

        self.ec2 = boto3.client("ec2",
                                region_name=default_region,
                                aws_access_key_id=self.creds['aws_access_key_id'],
                                aws_secret_access_key=self.creds['aws_secret_access_key'])
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
        next_token = ''
        try:
            ec2 = boto3.client("ec2",
                               region_name=region,
                               aws_access_key_id=self.creds['aws_access_key_id'],
                               aws_secret_access_key=self.creds['aws_secret_access_key'])
            data = ec2.describe_instances()
            if 'NextToken' in data:
                next_token = data['NextToken']
            while next_token:
                next_data = ec2.describe_instances(NextToken=next_token)
                data['Reservations'].append(next_data['Reservations'][0])
            del ec2

        except ClientError:
            self.logger.info(f'{region}: No instances found')
        except Exception as e:
            self.logger.error(f'Unknown Exception raised while attempting to obtain instances data:\n {e}')
            raise e

        if data:
            self.logger.info(f'{region}: instances found')
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
        if data:
            self.logger.info('Done gathering instance data')
        return data

    def write_to_file(self, file):
        with open(file, 'w') as f:
            f.write(str(self.get_data_from_all_regions()))
            self.logger.info(f'Data exported to file: {file}')
            return True
