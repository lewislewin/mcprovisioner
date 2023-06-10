import os
import json
from abc import ABC, abstractmethod

class ConfigValidator(ABC):
    @abstractmethod
    def validate(self):
        pass

class McProvisioner(ConfigValidator):
    CONFIG_FILE = 'config.json'
    REGIONS = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'eu-west-1', 'eu-west-2', 'eu-central-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'sa-east-1']
    REQUIRED_KEYS = ['aws_credentials']
    REQUIRED_DICT = {
        'aws_credentials': {
            'region': 'Please enter the AWS region',

        }
    }
    def __init__(self):
        #init config if present
        self.config = None
        self.initialize()

    def create_config(self):
        pass

    def initialize(self):
        print("Initializing mcprovisioner...")
        if not os.path.exists(self.CONFIG_FILE):
            print("Config file not found. Please create a config.json file.")
            return False
        
        with open(self.CONFIG_FILE) as config_file:
            try:
                self.config = json.load(config_file)
            except json.decoder.JSONDecodeError:
                print("Config file is not valid JSON.")
                return False
        
        return True

    def validate(self):
        for key in self.REQUIRED_KEYS:
            if key not in self.config:
                print("Config file is missing required key: " + key)
                return False
            
            if not isinstance(self.config[key], dict):
                print("Config file has an invalid value for key: " + key)
                return False
            
            if not self.config[key]:
                print("Config file has an empty value for key: " + key)
                return False
            
            for subkey in self.config[key]:
                if not self.config[key][subkey]:
                    print("Config file has an empty value for key: " + key + "." + subkey)
                    return False
                
                if not isinstance(self.config[key][subkey], str):
                    print("Config file has an invalid value for key: " + key + "." + subkey)
                    return False
                
                if subkey == 'region':
                    if self.config[key][subkey] not in self.REGIONS:
                        print("Config file has an invalid value for key: " + key + "." + subkey)
                        return False
                    
                if subkey == 'access_key_id':
                    if len(self.config[key][subkey]) != 20:
                        print("Config file has an invalid value for key: " + key + "." + subkey)
                        return False
        
        return True

    def run(self):
        if self.initialize() and self.validate():
            # Perform the main logic here
            print("Config file is valid. Starting the provisioning process...")
        else:
            print("Config validation failed. Unable to start the provisioning process.")

if __name__ == "__main__":
    mc_provisioner = McProvisioner()
    mc_provisioner.run()
