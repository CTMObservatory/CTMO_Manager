# -*- coding: utf-8 -*-
"""
Telescope Module

(c) GAIA-CTMO
"""
from loguru import logger
from nanpy import ArduinoApi, SerialManager
from time import sleep
import sys



class Arduino(object):
    def __init__(self, device):
        self.device = device
        self.ledPin = 7
        self.buttonPin = 8
        self.ledState = False
        self.buttonState = 0

    def setup(self):
        try:
            connection = SerialManager(device=self.device)
            self.ard = ArduinoApi(connection=connection)
        except:
            self.ard = None
            logger.error("Failed to connect to Arduino")
            return
         # Setup the pin modes
        self.ard.pinMode(self.ledPin, self.ard.OUTPUT)
        self.ard.pinMode(self.buttonPin, self.ard.INPUT)

    def turnOnLED(self):
        if not self.ledState:
            self.ard.digitalWrite(ledPin, self.ard.HIGH)
            self.ledState = True
            sleep(1)

    def turnOffLED(self):
        if self.ledState:
            self.ard.digitalWrite(ledPin, self.ard.LOW)
            self.ledState = False
            sleep(1)

_arduino = None

def front_desk(work_order):
    logger.info("Work order received.")
    logger.debug("{}".format(work_order))
    for k, v in work_order.items():
        print("{}:\t{}".format(k, v))
    return "Work order received."


def serve():
    logger.info("Started serving.")
    global _arduino
    try
        device = config.get_config_for_key('Dome Address').get('Arduino')
        _arduino = Arduino(device)
    except:
        logger.error("Error setting up Arduino")
    from xmlrpc.server import SimpleXMLRPCServer
    from . import config
    net_address = config.get_config_for_key('Dome Address')
    server = SimpleXMLRPCServer((net_address.get('IP'), net_address.get('Port')))
    server.register_function(front_desk, "front_desk")
    server.serve_forever()


if __name__ == '__main__':
    serve()
