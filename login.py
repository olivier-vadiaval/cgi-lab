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

if username == user and password == pwd:
    print("Set-Cookie: loggedIn = true;")
    print("Set-Cookie: username = " + user + ";")
    print("Set-Cookie: password = " + pwd + ";")
    print("Content-Type: text/html\r\n\r\n")
    print("Logged in\r\n <br>")
    print("Posted Data:", user, pwd)

else:
    print(after_login_incorrect())