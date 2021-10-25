from configurations.import_json_configuration import loaddata

NGROK_FILE_LOCATION=""
FETCHING_METHOD=""
NGROK_FILE_NAME=""
BACKEND_OS_NGROK=""

if __name__ == '__main__':
    NGROK_FILE_LOCATION,FETCHING_METHOD,NGROK_FILE_NAME,BACKEND_OS_NGROK = loaddata()