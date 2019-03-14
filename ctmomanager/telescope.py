# -*- coding: utf-8 -*-
"""
Scheduler Module

(c) GAIA-CTMO
"""
import yaml

CONFIG_PATH = '/etc/ctmo/ctmo.conf.yaml'
config = None
with open(CONFIG_PATH) as f:
    config = yaml.full_load(f.read())
net_address = config.get('Telescope Address')

def front_desk(work_order):
    for k, v in work_order.items():
        print("{}:\t{}".format(k, v))
    return "Work order received."

def serve():
    from xmlrpc.server import SimpleXMLRPCServer

    server = SimpleXMLRPCServer((net_address.get('IP'), net_address.get('Port')))
    server.register_function(front_desk, "front_desk")
    server.serve_forever()

if __name__ == '__main__':
    serve()
