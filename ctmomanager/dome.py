# -*- coding: utf-8 -*-
"""
Telescope Module

(c) GAIA-CTMO
"""
from loguru import logger
from nanpy import ArduinoApi, SerialManager
from . import config

domeconf = config.get_config_for_key("Dome Address")
connection = SerialManager(device=domeconf.get("Arduino"))
a = ArduinoApi(connection=connection)


def turn_led(state):
    global a
    ledPin = 7
    if state:
        a.digitalWrite(ledPin, a.HIGH)
    else:
        a.digitalWrite(ledPin, a.LOW)


def front_desk(work_order):
    global a
    ledPin = 7
    # Setup the pin modes
    a.pinMode(ledPin, a.OUTPUT)

    logger.info("Work order received.")
    logger.debug("{}".format(work_order))
    blink01 = work_order.get("Blink01")
    if blink01 is not None:
        turn_led(blink01)
    # for k, v in work_order.items():
    #     print("{}:\t{}".format(k, v))

    return "Work order received."


def serve():
    logger.info("Started serving.")
    from . import config

    # try:
    #     device = config.get_config_for_key('Dome Address').get('Arduino')
    #     _arduino = Arduino(device)
    # except:
    #     logger.error("Error setting up Arduino")
    from xmlrpc.server import SimpleXMLRPCServer

    net_address = config.get_config_for_key("Dome Address")
    server = SimpleXMLRPCServer((net_address.get("IP"), net_address.get("Port")))
    server.register_function(front_desk, "front_desk")
    server.serve_forever()


if __name__ == "__main__":
    serve()
