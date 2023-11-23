from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg

# https://github.com/fizista/micropython-umqtt.simple2/
from simple2 import MQTTClient

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x222222)

wifiCfg.doConnect('zpikiv', '78086975')

  
def sub_cb(topic, msg, retain, dup):
    print((topic, msg, retain, dup))

client = MQTTClient("id", 'test.mosquitto.org')
client.set_callback(sub_cb)
client.set_last_will('zpistatus', 'offline')
client.connect()
client.subscribe("zpitest")
client.publish('zpitest', 'Hello', retain=True)

while True:
    if blocking_method:
        client.wait_msg()
    else:
        client.check_msg()    
        wait(1)
client.disconnect()

# mosquitto_sub -t "zpitest" -v -h test.mosquitto.org
# mosquitto_pub -t "zpitest" -m "hello" -h test.mosquitto.org -r