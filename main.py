from configurations.import_json_configuration import loaddata
import requests
from clint.textui import progress
import os

from ngrok_core import NgRokCore


NGROK_FILE_LOCATION=""
FETCHING_METHOD=""
NGROK_FILE_NAME=""
BACKEND_OS_NGROK=""
ngcore


class Configration:
    def __init__(self):
        self.NGROK_FILE_LOCATION, self.FETCHING_METHOD, self.NGROK_FILE_NAME, self.BACKEND_OS_NGROK = loaddata()
        

def download_ngrok_file(ngrokresource,filename):
    config = Configration()
    print(f"------------ Downloading File {config.NGROK_FILE_NAME} : Progress ------------")

    r = requests.get(config.NGROK_FILE_LOCATION, stream=True)
    path = config.NGROK_FILE_NAME+".zip"
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

    print(f"------------ Downloading File {config.NGROK_FILE_NAME} : Completed ------------")

def setpasswd(passkey):
    """
        This function is set passwd for sshprocess for user:root, 
        When making a ssh session for remote instance. required a password for
        establishing secure connection

        example:
        >> ssh_ngrok.setpasswd("your-passkey")

        
    """
    os.system(f"echo  \"root:{passkey}\" | chpasswd > /dev/null")
    __setupconf__
    
def setauth(self,auth):
    ngrokcore = NgRokCore(authkey=auth)


def __setupconf__():

    """
    This function added the additional sshd configuration for remote connection
    """

    os.system("echo \"PasswordAuthentication yes\" > /etc/ssh/sshd_config")
    os.system("echo \"PermitUserEnvironment yes\" > /etc/ssh/sshd_config")
    os.system("echo \"PermitRootLogin yes\" > /etc/ssh/sshd_config")
    os.system("service ssh restart > /dev/null")



def main():
    config = Configration()
    download_ngrok_file(config.NGROK_FILE_LOCATION,config.NGROK_FILE_NAME)



if __name__ == '__main__':
    main()


