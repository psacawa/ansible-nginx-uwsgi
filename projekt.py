#!/usr/bin/env python

from datetime import datetime

def application(env, start_response):
    response = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    start_response ("200 OK", [( "content-type", "text/html" )])
    return bytes (response, 'utf-8')
