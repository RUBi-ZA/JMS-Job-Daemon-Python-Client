import requests, json

class JobDaemon(object):

    def __init__(self, host="127.0.0.1", port=80, token=None):
        self.host = host
        self.port = port
        self.token = token

    def get_status(self):
        return self._request("GET", "/status", {"token": self.token})

    def get_jobs(self):
        return self._request("GET", "/jobs", {"token": self.token})
    
    def _request(self, method, relative_url, params={}, json_str=None):
        method = getattr(requests, method)
        url = "%s:%d/%s" % (self.host, self.port, relative_url)

        response = method(url, params=params, json=json_str)

        try:
            return response.json()
        except Exception as err:
            print(err)
            raise Exception(response.text)
