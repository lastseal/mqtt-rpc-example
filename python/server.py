#!/usr/bin/python
# -*- coding: utf-8 -*-

from micro import mqtt
import time

@mqtt.rpc("status")
def status(data):
    return "OK"
  
@mqtt.rpc("change")
def change(data):
    print("change", data)
    return "OK"

while True:
    time.sleep(0.1)