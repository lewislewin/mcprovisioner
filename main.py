import os
import json
from lib.mcprovisioner import McProvisioner

#CONSTS
CONFIG_FILE = 'config.json'
REGIONS = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'eu-west-1', 'eu-west-2', 'eu-central-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'sa-east-1']
REQUIED_KEYS = ['aws_credentials']

def main():
    test = McProvisioner()
    test.validate()
    
                    

if __name__ == "__main__":
    main()