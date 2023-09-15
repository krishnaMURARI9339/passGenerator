import string
import random

if_name_="_main_"

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
len = int(input("Enter the length of password"))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#print(s)

random.shuffle(s)
print("Your password are :")
print("".join(s[0:len]))
