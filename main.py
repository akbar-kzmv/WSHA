import validators
from urllib.parse import urlparse
print("Web Security Header Analyzer 0.1")
program = True
while program:
    target = input("Enter the target URL: ")
    parsed_target = urlparse(target)
    if validators.url(target):
        print("URL Successful!")
        program = False
    else:
        print("Invalid URL. Try again!")
        
