# -*- coding: utf-8 -*-
"""
Scheduler Module

(c) GAIA-CTMO
"""
from loguru import logger
from . import config
import xmlrpc.client


def front_desk(work_order):
    logger.info("Work order received.")
    logger.debug("{}".format(work_order))
    for k, v in work_order.items():
        print("{}:\t{}".format(k, v))
    wotype = work_order.get('WOType')
    if wotype is None:
        logger.error("Missing key: WOType.")
        return
    if wotype == "Observation":
        # Send it over to telescope module
        telnet = config.get_config_for_key("Telescope Address")
        with xmlrpc.client.ServerProxy(telnet.get('HTTP')) as telescope_module:
            try:
                ret_string = telescope_module.front_desk(work_order)
                print(ret_string)
            except:
                logger.exception("Error connecting with Telescope.")
    elif wotype == "Dome":
        # Send it over to dome module
        telnet = config.get_config_for_key("Dome Address")
        with xmlrpc.client.ServerProxy(telnet.get('HTTP')) as dome_module:
            try:
                ret_string = dome_module.front_desk(work_order)
                print(ret_string)
            except:
                logger.exception("Error connecting with Dome.")
    return "Work order received."


def serve():
    logger.info("Started serving.")

    from xmlrpc.server import SimpleXMLRPCServer
    from . import config
    net_address = config.get_config_for_key('Scheduler Address')
    server = SimpleXMLRPCServer((net_address.get('IP'), net_address.get('Port')))
    server.register_function(front_desk, "front_desk")
    server.serve_forever()


if __name__ == '__main__':
    serve()
