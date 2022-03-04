import json
import requests
def ip_addre(ip):
    request_url = 'https://geolocation-db.com/jsonp/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    return result
ip_addre('2.2.2.2')