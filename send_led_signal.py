# -*- coding: utf-8 -*-
"""
Simple script to test if XMLRPC communication works.
(c) TOROS Project
"""
import xmlrpc.client
import yaml
import sys

CONFIG_PATH = '/etc/ctmo/ctmo.conf.yaml'
config = None
with open(CONFIG_PATH) as f:
    config = yaml.full_load(f.read())
network = config.get('Scheduler Address')


def send_work_order(turn_on=True):
    work_order = {
        "ID": "1",
        "WOType": "Dome",
        "Priority": 2,
        "Datetime": "2019-03-05T14:34:54.234",
        "User": "John Doe",
        "Blink01": turn_on,
    }
    with xmlrpc.client.ServerProxy(network.get('HTTP')) as scheduler_module:
        try:
            ret_string = scheduler_module.front_desk(work_order)
            print(ret_string)
        except Exception as err:
            print("Error connecting to scheduler.")
            print(err)


if __name__ == '__main__':
    turn_on = (sys.argv[1] == "on")
    print("Turning LED {}".format("on" if turn_on else "off"))
    send_work_order(turn_on)
