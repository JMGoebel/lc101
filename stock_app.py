import json
import urllib3
import certifi
import base64

ACCESS_KEYS = {
    'username': 'edb9e4be13e4d35a4aa8aedcc5cfd05d',
    'password': 'd93e8e9b3c773c04c11be21659d18594'
}

AUTH = base64.b64encode(b'edb9e4be13e4d35a4aa8aedcc5cfd05d:d93e8e9b3c773c04c11be21659d18594').decode("ascii")
print(AUTH)

ACCESS_POINT = "https://api.intrinio.com/"

def get_json(url, endpoint):
    ''' grab some json and returns a <dict> '''
    #setup pool manager
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    #Make Request
    print("TARGET: " + url + endpoint)
    req = http.request(
        'GET',
        url + endpoint,
        headers = {
            "Authorization": "Basic %s" % AUTH
        }
    )

    return json.loads(req.data)

data = get_json(ACCESS_POINT, "companies?ticker=RHHBY:OTC")

for key in data:
    print("{}: {}".format(key, data[key]))
