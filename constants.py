import os
"""
This file contains constants that are used throughout the code
in order to not pollute the code all the hard coded variables are located here
"""
DEFAULT_REGION = 'us-east-2'
DEFAULT_DATA_FILE_PATH = os.path.join(os.getcwd(), 'test_data_file.txt')
CREDS_FILE_PATH = os.path.join(os.path.expanduser('~'), '.aws\\credentials')
LOG_FILE_PATH = os.path.join(os.getcwd(), 'log.txt')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s | %(message)s'

# note that the RAM_COMPARISON_TABLE is not complete
# there are over 100 different machine types, this table is a general containing the main machine types
RAM_COMPARISON_TABLE = {'t2.nano': '0.5GB',
                        't2.micro': '1GB',
                        't2.small': '2GB',
                        't2.medium': '4GB',
                        't2.large': '8GB',
                        't2.xlarge': '16GB',
                        't2.2xlarge': '32GB',
                        'mac1.metal': '32GB',
                        't4g.nano': '0.5GB',
                        't4g.micro': '1GB',
                        't4g.small': '2GB',
                        't4g.medium': '4GB',
                        't4g.large': '8GB',
                        't4g.xlarge': '16GB',
                        't4g.2xlarge': '32GB',
                        't3.nano': '0.5GB',
                        't3.micro': '1GB',
                        't3.small': '2GB',
                        't3.medium': '4GB',
                        't3.large': '8GB',
                        't3.xlarge': '16GB',
                        't3.2xlarge': '32GB',
                        't3a.nano': '0.5GB',
                        't3a.micro': '1GB',
                        't3a.small': '2GB',
                        't3a.medium': '4GB',
                        't3a.large': '8GB',
                        't3a.xlarge': '16GB',
                        't3a.2xlarge': '32GB',}

