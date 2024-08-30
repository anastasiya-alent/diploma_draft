import requests
import allure

class apiClass:

    def __init__(self, url):
        self.url = url

# получит токен авторизации

    def get_token(self):
        auth_headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDIwMTA4LCJpYXQiOjE3MjUwMTcwMzQsImV4cCI6MTcyNTAyMDYzNCwidHlwZSI6MjB9.NyLS20IOA0ByoawLbcgObGLwE4uuIg6MiRlvHYNaZDA'
        }
        return auth_headers
    
    def get(self, request_url, auth_headers):

        with allure.step ("GET запросы"):
            response = requests.get(self.url + request_url, headers=auth_headers)
            return response
    
    def post(self, request_url, auth_headers):

        with allure.step ("POST запросы"):
            response = requests.post(self.url + request_url, headers=auth_headers)
            return response