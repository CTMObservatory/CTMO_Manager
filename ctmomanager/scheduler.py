# -*- coding: utf-8 -*-
"""
Scheduler Module

(c) GAIA-CTMO
"""
from loguru import logger
from . import config
import xmlrpc.client


def front_desk(work_order):
    """Front Desk will receive your Work Order and dispatch it to the appropriate service.
Make sure all your services are running."""
    logger.info("Work order received.")
    logger.debug("{}".format(work_order))
    for k, v in work_order.items():
        print("{}:\t{}".format(k, v))
    wotype = work_order.get("WOType")
    if wotype is None:
        logger.error("Missing key: WOType.")
        return
    if wotype == "Observation":
        # Send it over to telescope module
        telnet = config.get_config_for_key("Telescope Address")
        with xmlrpc.client.ServerProxy(telnet.get("HTTP")) as telescope_module:
            try:
                ret_string = telescope_module.front_desk(work_order)
                print(ret_string)
            except:
                logger.exception("Error connecting with Telescope.")
    elif wotype == "Dome":
        # Send it over to dome module
        telnet = config.get_config_for_key("Dome Address")
        with xmlrpc.client.ServerProxy(telnet.get("HTTP")) as dome_module:
            try:
                ret_string = dome_module.front_desk(work_order)
                print(ret_string)
            except:
                logger.exception("Error connecting with Dome.")
    return "Work order received."


def serve():
    logger.info("Started serving.")

    from xmlrpc.server import DocXMLRPCServer
    from xmlrpc.server import DocXMLRPCRequestHandler
    from . import config

    # A request handler that responds appropriately for CORS and preflight
    class CORSRequestHandler(DocXMLRPCRequestHandler):
        def do_OPTIONS(self):
            self.send_response(200)
            self.end_headers()

        # Add these headers to all responses
        def end_headers(self):
            self.send_header(
                "Access-Control-Allow-Headers",
                "Origin, X-Requested-With, Content-Type, Accept",
            )
            self.send_header("Access-Control-Allow-Origin", "*")
            super().end_headers()

    net_address = config.get_config_for_key("Scheduler Address")
    server = DocXMLRPCServer(
        ("0.0.0.0", net_address.get("Port")), requestHandler=CORSRequestHandler
    )
    server.set_server_title("Scheduler Docs")
    server.set_server_name("CTMO Scheduler Service")
    server.set_server_documentation(
        "The scheduler module exports only the front_desk method through the XML-RPC protocol."
    )
    server.register_function(front_desk)
    server.serve_forever()


if __name__ == "__main__":
    serve()
