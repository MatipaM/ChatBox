# API
import base64
import http.client
import json
import urllib.parse
import ssl

class API():

    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def query_ai(self, query):
        encoded_query = urllib.parse.quote(query)
        path = f"/api?query={encoded_query}"

        conn = http.client.HTTPSConnection(base64.b64decode("YWkxLnJlZHNoaWZ0ZWQuY28udWs=".encode('utf-8')).decode('utf-8'), context=ssl._create_unverified_context())
        # conn = http.client.HTTPSConnection(base64.b64decode("YWkxLnJlZHNoaWZ0ZWQuY28udWs=".encode('utf-8')).decode('utf-8'))

        try:
            conn.request("GET", path)
            response = conn.getresponse()

            if response.status == 200:
                data = response.read().decode()
                return json.loads(data)
            else:
                print(f"Request failed with status code: {response.status}")
        finally:
            conn.close()

            

