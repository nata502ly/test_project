import requests
class PulseRestApi:
    def __init__(self):
        self.host = "pulse-rest-testing.herokuapp.com"
        self.base_url = "http://{}/".format(self.host)
    def create_object(self,obj):
        url = self.base_url + obj.url + "/"
        response = requests.post(url, data = obj.get_dict())
    def get_object(self,obj):
        url = self.base_url + obj.url + "/" + str(obj.id) + "/"
        response = requests.get(url)
        return response