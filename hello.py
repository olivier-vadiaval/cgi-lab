#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import os
from templates import *

form = cgi.FieldStorage()

print("Content-Type: text/html")
print()
print("<html>")
print("<H1>" + os.environ.get("QUERY_STRING") + "</H1>")
print("<H1>" + os.environ.get("HTTP_USER_AGENT") + "</H1>")
print(login_page())
print(os.environ)
print("</html>")