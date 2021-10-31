import os
class NgRokCore:

    def __init__(self,authkey):
        self.authkey = authkey

    def runupcore(self):
        os.run(f'./ngrok authtoken {self.authkey}')
        
        