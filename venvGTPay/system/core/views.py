import requests
from django.http import HttpResponse

def make_payment(request):
    api_url = "https://myghpay.com/myghpayclient/"

    payload = {
        "ClientID": 'ab37d480-4545-48d0-b6f2-afc3ff87c8a6',
        "ClientSecret": 'e46f1074-ae57-4002-80f1-d60bfa484cfe',
        "Amount": '1000',
        "ReturnURL": 'https://3dwirelessplus.com/',
        #'secureHash': '97db4f60a173bfb3f113939d3a00af32',
    }

    try:
        # Make a POST request to the payment API endpoint
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            # If the response is HTML, return it as is
            if 'text/html' in response.headers.get('content-type', ''):
            	return HttpResponse(response.content, content_type='text/html')

        # Handle other response types or errors here
        return HttpResponse("Unexpected response from the API.", status=500)

    except requests.RequestException as e:
        # Handle request exceptions
        return HttpResponse("Request Exception: " + str(e), status=500)
