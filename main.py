print("Web Security Header Analyzer 0.1")
program = True
while program:
    user_value = input("Enter the target URL: ")
    if not (user_value.startswith("http://") or user_value.startswith("https://")):
        print("Invalid URL! Please enter again")
    else:
        print(f"Target: {user_value}")
        program = False
