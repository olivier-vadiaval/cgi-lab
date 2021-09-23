#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
cgitb.enable()

import os
from time import gmtime, strftime
from templates import *
from secret import *

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<H1>" + os.environ.get("QUERY_STRING") + "</H1>")
print("<H1>" + os.environ.get("HTTP_USER_AGENT") + "</H1>")
print(login_page())
print(os.environ)
print("</html>")