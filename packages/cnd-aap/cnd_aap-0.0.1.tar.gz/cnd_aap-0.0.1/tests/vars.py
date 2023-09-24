import cndprint
import yaml


creds = {"username": '', "password": ''}
host = 'https://iamnotexisting.com'
_print = cndprint.CndPrint(level="log", uuid=">> ", silent_mode=False)

def read_file(filename):
    return open(filename).read()
    
def read_yaml_file(filename):
    content = read_file(filename)
    return yaml.safe_load(content)
