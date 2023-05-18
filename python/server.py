#!/usr/bin/python
# -*- coding: utf-8 -*-

from micro import mqtt

@mqtt.rpc("status")
def status(data):
    return "OK"
  
@mqtt.rpc("change")
def status(data):
    return "OK"
