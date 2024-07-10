

import os, json

try:
    import requests
except:
    os.system("pip install requests")
    import requests


class PyPiSearch():
    def __init__(self):
        self.base_url = "https://pypi.org/pypi/<packageName>/json"

    def search(self, packageName:str):
        thisPageRequest = requests.get(f"https://pypi.org/pypi/{packageName}/json")

        if thisPageRequest.status_code != 200:
            return {
                "success": False,
                "errorType": "ModuleImportError",
                "message": "The pypi server returned a {thisPageRequest.status_code} response code."
            }
        
        thisPackageJsonData = thisPageRequest.json()
        #print(json.dumps(thisPackageJsonData, indent=4))

        return {
            "success": True,
            "data": thisPackageJsonData
        }
    