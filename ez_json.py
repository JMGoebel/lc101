''' Small library to quickly recieve json requires json urllib3 certifi'''

import json
import urllib3
import certifi

def get_json(target, endpoint):
    ''' grab some json and returns a <dict> '''
    #setup pool manager
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    #Make Request
    req = http.request('GET', target + endpoint)
    return json.loads(req.data)

def post_json(target, endpoint, data):
    ''' grab some json and returns a <dict> '''
    #setup pool manager
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    
    #Data must be of type <dict>
    if(type(data) == 'dict'):
        encoded_data = json.dumps(data).encode('utf-8')
    else:
        print("Data must be of type <dict>")
    
    req = http.request(
        'POST', 
        target + endpoint,
        body=encoded_data,
        headers={'Content-Type': 'application/json'}
    )
    return print(req.status)


def main():
    data = get_json('https://api.iextrading.com/1.0/stock/fb/quote','')
    print(data['symbol'])
    print(data['open'])
    print(data['close'])
if __name__ == "__main__":
    main()
