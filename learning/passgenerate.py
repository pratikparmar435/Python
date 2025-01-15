import string
import random

charValues = string.ascii_letters + string.digits + string.punctuation


pass_len = int(input("Enter length of password:"))

# password = ""
# for i in range(1,pass_len+1):
#     password += random.choice(charValues)
#or
#list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])
print(password)

