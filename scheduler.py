# -*- coding: utf-8 -*-

"""
Scheduler Module

This is just a file to write first attempts at a scheduler module.

(c) TOROS Project
"""


import xmlrpc.client
TELESCOPE_IP = "http://localhost:8000/"


def send_work_order():
    work_order = {
        "Priority": 1,
        "Coordinates": {"RA": 23.1, "Dec": 13.2},
        "Filter": "I",
        "Author": "Main Module"
    }

    with xmlrpc.client.ServerProxy(TELESCOPE_IP) as telescope_module:
        try:
            telescope_module.front_desk(work_order)
        except xmlrpc.client.ProtocolError as err:
            print("A protocol error occurred")
            print("URL: %s" % err.url)
            print("HTTP/HTTPS headers: %s" % err.headers)
            print("Error code: %d" % err.errcode)
            print("Error message: %s" % err.errmsg)


if __name__ == '__main__':
    send_work_order()
