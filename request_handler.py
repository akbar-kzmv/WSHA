import requests
def send_request(request):
    response = requests.get(request)
    return response
