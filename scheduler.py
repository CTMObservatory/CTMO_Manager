# -*- coding: utf-8 -*-
"""
Scheduler Module

(c) TOROS Project
"""
from xmlrpc.server import SimpleXMLRPCServer
import datetime
import xmlrpc.client

 
def is_even(n):
     return n % 2 == 0

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def front_desk(work_order):
    return "Work order received."

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(is_even, "is_even")
server.register_function(today, "today")
server.register_function(front_desk, "front_desk")
server.serve_forever()
