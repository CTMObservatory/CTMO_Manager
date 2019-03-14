# -*- coding: utf-8 -*-
"""
Scheduler Module

(c) GAIA-CTMO
"""
def front_desk(work_order):
    for k, v in work_order.items():
        print("{}:\t{}".format(k, v))
    return "Work order received."


def serve():
    from xmlrpc.server import SimpleXMLRPCServer
    from . import config
    net_address = config.get_config_for_key('Scheduler Address')
    server = SimpleXMLRPCServer((net_address.get('IP'), net_address.get('Port')))
    server.register_function(front_desk, "front_desk")
    server.serve_forever()


if __name__ == '__main__':
    serve()
