# -*- coding: utf-8 -*

from micro import mqtt

res = mqtt.call("status")
print(res)
