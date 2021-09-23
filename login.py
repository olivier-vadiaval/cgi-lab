#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import os
from templates import *

form = cgi.FieldStorage()
username = form.getvalue("username")
pwd = form.getvalue("password")

print("Content-Type: text/html")
print()
print("<html>")
print("<H1>Username: " + username + "</H1>")
print("<H1>Password: " + pwd + "</H1>")
print("</html>")