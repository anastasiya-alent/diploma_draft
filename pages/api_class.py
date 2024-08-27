import requests

class apiClass:

    def __init__(self, url):
        self.url = url

# получит токен авторизации

    def get_token(self):
        auth_headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDIwMTA4LCJpYXQiOjE3MjQ3MDAxMTQsImV4cCI6MTcyNDcwMzcxNCwidHlwZSI6MjB9.RPp1-zYq-9J_sFlhZZ2joDmpOPcaMaU0alffxspW9g8'
        }
        return auth_headers
    
    def get(self, request_url, auth_headers):
        response = requests.get(self.url + request_url, headers=auth_headers)
        return response
    
    def post(self, request_url, auth_headers):
        response = requests.post(self.url + request_url, headers=auth_headers)
        return response