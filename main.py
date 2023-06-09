import os
import json

#CONSTS
CONFIG_FILE = 'config.json'
REGIONS = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'eu-west-1', 'eu-west-2', 'eu-central-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'sa-east-1']
REQUIED_KEYS = ['aws_credentials']

def main():
    print("Initialising mcprovisioner...")

    if not os.path.exists(CONFIG_FILE):
        #TODO: Create config file automatically
        print("Config file not found. Please create a config.json file.")
        return
    
    with open(CONFIG_FILE) as config_file:
        try:
            config = json.load(config_file)
        except json.decoder.JSONDecodeError:
            print("Config file is not valid JSON.")
            return

        for key in REQUIED_KEYS:
            if key not in config:
                print("Config file is missing required key: " + key)
                return
            
            if not isinstance(config[key], dict):
                print("Config file has invalid value for key: " + key)
                return
            
            if not config[key]:
                print("Config file has empty value for key: " + key)
                return
            
            for subkey in config[key]:
                if not config[key][subkey]:
                    print("Config file has empty value for key: " + key + "." + subkey)
                    return
                
                if not isinstance(config[key][subkey], str):
                    print("Config file has invalid value for key: " + key + "." + subkey)
                    return
                
                if subkey == 'region':
                    if config[key][subkey] not in REGIONS:
                        print("Config file has invalid value for key: " + key + "." + subkey)
                        return
                    
                if subkey == 'access_key_id':
                    if len(config[key][subkey]) != 20:
                        print("Config file has invalid value for key: " + key + "." + subkey)
                        return
                    

if __name__ == "__main__":
    main()