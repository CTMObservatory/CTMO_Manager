# -*- coding: utf-8 -*-
"""
Telescope Module

(c) GAIA-CTMO
"""
import logging


def front_desk(work_order):
    logger = logging.getLogger(__name__)
    logger.info("Work order received.")
    logger.debug("{}".format(work_order))
    for k, v in work_order.items():
        print("{}:\t{}".format(k, v))
    return "Work order received."


def serve():
    logger = logging.getLogger(__name__)
    logger.info("Started serving.")
    from xmlrpc.server import SimpleXMLRPCServer
    from . import config
    net_address = config.get_config_for_key('Telescope Address')
    server = SimpleXMLRPCServer((net_address.get('IP'), net_address.get('Port')))
    server.register_function(front_desk, "front_desk")
    server.serve_forever()


if __name__ == '__main__':
    serve()
