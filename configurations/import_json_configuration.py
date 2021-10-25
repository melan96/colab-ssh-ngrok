import json

def loaddata():
    with open('configurations/colab-ssh-ngrok.json') as config_json_file:
        config_data = json.load(config_json_file)['ngrok_download_resource']

        return config_data['resource_url'],\
               config_data['fetching_method'],\
               config_data['ngrok_file_name'],\
               config_data['backend_os_ngrok']