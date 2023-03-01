import requests
import os
from dotenv import load_dotenv
import json
################################
class Vcenterapi:
    def __init__(self) -> None:
        load_dotenv()
        self.headers={}
        self.URL=f"""https://{os.environ['URL']}/rest/vcenter"""
        
    #Lectura del header
    def get_header(self):
        print(self.headers)

    def loggin(self):
        r = requests.post(f"""https://{os.environ['URL']}/api/session""", auth=(os.environ['USERR'], os.environ['PASS']), verify=False)
        TOKEN= r.text.replace('"','')
        self.headers = {
                        'vmware-api-session-id': f"""{TOKEN}"""
                    }

    def getAllVm(self):
        vm = requests.get(f"""{self.URL}/vm""", headers=self.headers, verify=False)
        return json.loads(vm.text)

        """
        RECORRER LOS ELEMENTOS DE ESTE JSON
        for v in vm["value"]:
            print(v["name"]) """

    def getVm(self,id):
        print(f"""header: {self.headers}""")
        vm = requests.get(f"""{self.URL}/vm/{id}""", headers=self.headers, verify=False)
        vm = json.loads(vm.text)
        print(vm)


