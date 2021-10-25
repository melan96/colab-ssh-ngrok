import json

def loaddata():
    with open('colab-ssh-ngrok.json') as config_json_file:
        config_data = json.load(config_json_file)
        return config_data['ngrok_download_resource']['resource_url'],\
               config_data['ngrok_download_resource']['fetching_method'],\
               config_data['ngrok_download_resource']['ngrok_file_name'],\
               config_data['ngrok_download_resource']['backend_os_ngrok']