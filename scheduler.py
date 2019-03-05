# -*- coding: utf-8 -*-
"""
Scheduler Module

(c) TOROS Project
"""
import datetime
import xmlrpc.client
import yaml

__version__ = '0.1a2'

def is_even(n):
     return n % 2 == 0

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def front_desk(work_order):
    return "Work order received."

def serve():
    from xmlrpc.server import SimpleXMLRPCServer

    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_function(is_even, "is_even")
    server.register_function(today, "today")
    server.register_function(front_desk, "front_desk")
    server.serve_forever()

if __name__ == '__main__':
    serve()
