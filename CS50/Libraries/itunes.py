#-------------------------------------------------------------
# Using request package I've just downloaded using pip install request.
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
#sys.exit() use to exit whole program where break is use to exit just the loop.
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
# json - java script object notation.

o = response.json()
for result in o["results"]:
    print(result["trackName"])


#---------------------------------------------------------------------------------

