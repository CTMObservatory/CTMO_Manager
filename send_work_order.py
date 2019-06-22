# -*- coding: utf-8 -*-
"""
Simple script to test if XMLRPC communication works.
(c) TOROS Project
"""
import xmlrpc.client
import yaml

CONFIG_PATH = "/etc/ctmo/ctmo.conf.yaml"
config = None
with open(CONFIG_PATH) as f:
    config = yaml.full_load(f.read())
network = config.get("Scheduler Address")


def send_work_order():
    print("Sending work order to telescope")
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
    with xmlrpc.client.ServerProxy(network.get("HTTP")) as scheduler_module:
        try:
            ret_string = scheduler_module.front_desk(work_order)
            print(ret_string)
        except Exception as err:
            print("Error connecting to scheduler.")
            print(err)

    print("Sending work order to dome")
    work_order = {
        "ID": "1",
        "WOType": "Dome",
        "Priority": 2,
        "Datetime": "2019-03-05T14:34:54.234",
        "User": "John Doe",
        "Blink01": True,
    }
    with xmlrpc.client.ServerProxy(network.get("HTTP")) as scheduler_module:
        try:
            ret_string = scheduler_module.front_desk(work_order)
            print(ret_string)
        except Exception as err:
            print("Error connecting to scheduler.")
            print(err)

def send_wo_raw():
    import requests
    work_order = {
        "ID": "1",
        "WOType": "Dome",
        "Priority": 2,
        "Datetime": "2019-03-05T14:34:54.234",
        "User": "John Doe",
        "Blink01": True,
    }

    # This converts the python dict work_order into an xml equivalent request
    import xmlrpc.client
    wo_xml = xmlrpc.client.dumps((work_order,), "front_desk")
    # print(wo_xml)

    url = "http://localhost:8000"
    req = requests.post(url, data=wo_xml, headers={"Content-Type": "text/xml"})
    print("Request Header:")
    print("===============")
    print(req.request.headers)
    print("\nRequest Response:")
    print("=================")
    print(req.text)


if __name__ == "__main__":
    send_work_order()
    # send_wo_raw()
