#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
cgitb.enable()

import os
from secret import *
from templates import *

form = cgi.FieldStorage()
user = form.getvalue("username")
pwd = form.getvalue("password")

cookies = os.environ.get("HTTP_COOKIE").split(";")

if username == user and password == pwd:
    print("Set-Cookie: username = " + username + ";")
    print("Set-Cookie: password = " + password + ";")

print("Content-Type: text/html\r\n\r\n")
print("Logged in")

if len(cookies) == 2:
    print(secret_page(user, pwd))