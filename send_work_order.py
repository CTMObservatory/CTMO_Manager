# -*- coding: utf-8 -*-
"""
Simple script to test if XMLRPC communication works.
(c) TOROS Project
"""
import xmlrpc.client
import yaml

CONFIG_PATH = '/etc/ctmo/ctmo.conf.yaml'
config = None
with open(CONFIG_PATH) as f:
    config = yaml.full_load(f.read())
network = config.get('Scheduler Address')


def send_work_order():
    work_order = {
        "ID": "1",
        "WOType": "Observation",
        "Telescope Name": "CTMO",
        "RA": 23.1,
        "Dec": 13.2,
        "Filter": "I",
        "Exposure Time": 30.0,
        "Number of Exposures": 1,
        "Priority": 1.3,
        "Datetime": "2019-03-05T14:34:54.234",
        "User": "Main Module",
        "Type of job": "Research",
        "Type of object": "Galaxy",
        "Calibration Frames": "Yes",
        "Output": "Analysis",
    }

    with xmlrpc.client.ServerProxy(network.get('HTTP')) as scheduler_module:
        try:
            ret_string = scheduler_module.front_desk(work_order)
            print(ret_string)
        except Exception as err:
            print("Error connecting to scheduler.")
            print(err)


if __name__ == '__main__':
    send_work_order()
