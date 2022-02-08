import typing
from dataclasses import dataclass
from constants import RAM_COMPARISON_TABLE
import datetime


def datetime_handler(x):
    """
    convert datetime objects to the iso format for dates
    :param x: datetime func
    :return: string - formatted iso time
    """
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")


@dataclass
class IDInfo:
    owner_id: str
    image_id: str
    instance_id: str


@dataclass
class OSInfo:
    platform_details: str
    architecture: str
    root_device_name: str
    root_type: str


@dataclass
class NetworkInfo:
    private_ip_address: str
    private_dns_name: str
    mac_address: str
    subnet_id: str
    interface_type: str
    interface_id: str
    status: str
    groups: list


@dataclass
class SpecsInfo:
    def __init__(self, cpu, instance_type):
        self.cpu: dict = cpu
        self.instance_type: str = instance_type
        self.ram: str = RAM_COMPARISON_TABLE[instance_type]

    def __repr__(self):
        return f'cpu:{self.cpu}, instance_ype:{self.instance_type}, ram:{self.ram}'


@dataclass
class Instance:
    id_info: type(IDInfo)
    os_info: type(OSInfo)
    network_info: type(NetworkInfo)
    specs_info: type(SpecsInfo)
    status: str
    keyname_description: str
    launch_time: str
    tags: list
    security_groups: list
    client_token: str


class InstancesInformation:
    """
    handles all the information extraction and sorts it in a dictionary
    in order where key is the instance id and the value is the information
    about the instance itself
    """
    def __init__(self, information_dictionary):
        self.information_dictionary: dict = information_dictionary
        self.instances = {}
        self._extract_information()

    def __repr__(self):
        return str(self.instances)

    def _extract_information(self):
        """
        loops over every instance and collects information about it, then updates the self.instances
        variable
        :return:
        """
        for reservations in self.information_dictionary['Reservations']:
            for instance in reservations['Instances']:
                network = instance['NetworkInterfaces'][0]

                id_info = IDInfo(network['OwnerId'],
                                 instance['ImageId'],
                                 instance['InstanceId'])

                os_info = OSInfo(instance['PlatformDetails'],
                                 instance['Architecture'],
                                 instance['RootDeviceName'],
                                 instance['RootDeviceType'])

                network_info = NetworkInfo(network['PrivateIpAddress'],
                                           network['PrivateDnsName'],
                                           network['MacAddress'],
                                           network['SubnetId'],
                                           network['InterfaceType'],
                                           network['NetworkInterfaceId'],
                                           network['Status'],
                                           network['Groups'])

                specs_info = SpecsInfo(instance['CpuOptions'],
                                       instance['InstanceType'])

                status = instance['State']['Name']
                keyname_description = instance['KeyName']
                launch_time = datetime_handler(instance['LaunchTime'])
                tags = instance['Tags']
                security_groups = instance['SecurityGroups']
                client_token = instance['ClientToken']

                self.instances[instance['InstanceId']] = Instance(id_info,
                                                                  os_info,
                                                                  network_info,
                                                                  specs_info,
                                                                  status,
                                                                  keyname_description,
                                                                  launch_time,
                                                                  tags,
                                                                  security_groups,
                                                                  client_token)
