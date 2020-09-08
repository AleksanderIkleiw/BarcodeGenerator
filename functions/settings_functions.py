import yaml
import os


def read_settings():
    with open(f"{os.getcwd().split('user_interface')[0]}\\settings.yaml") as f:
        data = yaml.full_load(f)
        return data

def write_data(data):
    print(data)
    with open(f"{os.getcwd().split('user_interface')[0]}\\settings.yaml", 'w') as f:
        yaml.dump(data, f, sort_keys=False)

