#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
cgitb.enable()

import os
from time import gmtime, strftime
from templates import *

is_logged = False
user = ""
pwd = ""
http_cookie = os.environ.get("HTTP_COOKIE")
if len(http_cookie) > 0:
    cookies = http_cookie.split("; ")
    for cookie in cookies:
        cookie_key = cookie.split("=")[0]
        cookie_value = cookie.split("=")[1]
        if cookie_key == "loggedIn":
            is_logged = cookie_value
        if cookie_key == "username":
            user = cookie_value
        if cookie_key == "password":
            pwd = cookie_value

if is_logged:
    print("Content-Type: text/html\r\n\r\n")
    print(secret_page(user, pwd))

else:
    print("Content-Type: text/html\r\n\r\n")
    print("<html>")
    print("<H1>" + os.environ.get("QUERY_STRING") + "</H1>")
    print("<H1>" + os.environ.get("HTTP_USER_AGENT") + "</H1>")
    print(login_page())
    print(os.environ)
    print("</html>")