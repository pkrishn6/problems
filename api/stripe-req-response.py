import requests
import json

class Stripe(object):
    def validate_request(self, content):
        request = content['request']
        response = content['response']
        headers = request['headers']
        url = 'https://' + request['headers']['Host'] + request['url']
        data = request['body']
        method = request['method']

        # error checking
        r = requests.request(method, url=url, data=data, headers=headers)
        print(r.json())
        if r.status_code != response['code']:
            print("status codes do not match", r.status_code, response['code'])
            return False
        return True

    def sendReq(self, fp):
        with open(fp) as json_file:
            content = json.load(json_file)
        for i in range(len(content)):
            req_resp = content[i]
            if not self.validate_request(req_resp):
                print("Validation failed for", i)
                break
            else:
                print(f"request:{i} passed")

s = Stripe()
s.sendReq('requestlog-charges.json')
