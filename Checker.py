
import requests
import os

os.system("clear")
blue = '\033[94m'
cyan= '\033[96m'
green = '\033[92m'
warning = '\033[93m'
fail= '\033[91m'
end= '\033[0m'

kartik = """
 _  __         _____ _ _
| |/ /__ _ _ _|_   _(_) | __
| ' // _` | '__|| | | | |/ /
| . \ (_| | |   | | | |   <
|_|\_\__,_|_|   |_| |_|_|\_\
"""
print(kartik)
print("\n\n")
print("1. check from txt file\n2. check manually")
a = int(input("\nenter ur choice ==> "))
print("\n")

if a == 1:
print("make a txt file of gmails [recommended same location]\n")
m = input("enter ur file name.. if have in other location then enter full path\n==>")
c = ""
with open(m, "r") as f:
c += f.read()
c = c.split("\n")
for item in c:
x = requests.Session()
d = x.get(f'https://mail.google.com/mail/gxlu?email={item}')
e = d.cookies
e = e.get_dict()
if len(e) != 0:
print(f"{green}{item}{end}")
with open("valid.txt", "a") as f:
f.write(f"{item}\n")
else:
print(f"{fail}{item}{end}")
elif a == 2:
print("Example: valid@gmail.com email@gmail.com\n[gib a s

pace between each gmail --> it will not write in file(valid

.txt)] \n\n")

a = input("enter gmails: ")
b = a.split()
for item in b:
x = requests.Session()
c = x.get(f'https://mail.google.com/mail/gxlu?email={item}')

d = c.cookies
d = d.get_dict()
if len(d) != 0:

print(f"{green}{item}{end}")

else:
print(f"{fail}{item}{end}")
else:

print("Invalid input")










