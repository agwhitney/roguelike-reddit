import json


config_file = "config_files/settings.json"

with open(config_file, 'r') as f:
    settings = json.load(f)
