import validators
from urllib.parse import urlparse
from request_handler import send_request
from output import display_response

print("Web Security Header Analyzer 0.1")
program = True
while program:
    target = input("Enter the target URL: ")
    parsed_target = urlparse(target)
    if validators.url(target):
        program = False
    else:
        print("Invalid URL. Try again!")

response = send_request(target)
display_response(response, target)

    
