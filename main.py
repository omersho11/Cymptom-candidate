from ec2_client import EC2Client
from log_handler import Logger

logger = Logger()
"""
this is an example of how easy it is to use the EC2Client
this is not the testsuite
"""


def main():
    c = EC2Client(logger)
    c.get_data_from_all_regions()


if __name__ == '__main__':
    main()
