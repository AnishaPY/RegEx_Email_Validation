import re
email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email id : ")

if re.search(email_condition, user_email):
    print("Your email is valid.")
else:
    print("Your email is not valid.")