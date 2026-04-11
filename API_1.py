import requests
import sys
import json


if len(sys.argv)!=2:
    sys.exit("we are out")

response = requests.get("https://api.github.com/users/" +sys.argv[1])
print(json.dumps(response.json(),indent=2))