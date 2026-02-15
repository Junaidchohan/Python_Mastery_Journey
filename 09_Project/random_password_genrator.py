import random
import string


pass_len = 12
charValues = string.ascii_letters + string.punctuation + string.digits

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)
# print("Your random password is:", password)

password = "".join([random.choice(charValues) for i in range(pass_len)])
print("Your random password is:", password)


