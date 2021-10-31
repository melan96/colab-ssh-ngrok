import os
import requests


class NgRokCore:

    def __init__(self,authkey):
        self.authkey = authkey
        self.tunnel_api = "http://localhost:4040/api/tunnels"

    def runupcore(self):
        os.run(f'./ngrok authtoken {self.authkey} && ./ngrok tcp 22 &')

    def tunnel_report(self):
        print(print(requests.get(self.tunnel_api).json()))



        