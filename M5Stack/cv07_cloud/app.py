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
client = MQTTClient("id", 'test.mosquitto.org')

led = M5Led(x=20, y=10, w=25, h=25, color=0x00ff00)
s1 = M5Switch(x=10, y=50, w=100, h=50)
s2 = M5Switch(x=10, y=110, w=100, h=50)
s3 = M5Switch(x=10, y=170, w=100, h=50)

def s1On():
    client.publish('piv/device1/stat/switch1', 'on', retain=True)
s1.on(s1On)
def s1Off():
    client.publish('piv/device1/stat/switch1', 'off', retain=True)
s1.off(s1Off)
def s2On():
    client.publish('piv/device1/stat/switch2', 'on', retain=True)
s2.on(s2On)
def s2Off():
    client.publish('piv/device1/stat/switch2', 'off', retain=True)
s2.off(s2Off)
def s3On():
    client.publish('piv/device1/stat/switch3', 'on', retain=True)
s3.on(s3On)
def s3Off():
    client.publish('piv/device1/stat/switch3', 'off', retain=True)
s3.off(s3Off)

def pressedA():
    sw = {}
    sw["switch1"]=s1.get_state()
    sw["switch2"]=s2.get_state()
    sw["switch3"]=s3.get_state()
    client.publish('piv/device1/stat/switches', str(sw), retain=True)
btnA.wasPressed(pressedA)
def pressedB():
    client.publish('piv/device1/stat/button1', '{\"event_type\": \"press\"}', retain=False)
btnB.wasPressed(pressedB)

def sub_cb(topic, msg, retain, dup):
    topic = topic.decode('UTF-8')
    msg = msg.decode('UTF-8')
    if topic == 'piv/device1/cmnd/led1':
        if msg == 'on':
            led.set_on()
        else:
            led.set_off()
    if topic == 'piv/device1/cmnd/switch1':
        if msg == 'on':
            s1.set_on()
        else:
            s1.set_off()
    if topic == 'piv/device1/cmnd/switch2':
        if msg == 'on':
            s2.set_on()
        else:
            s2.set_off()
    if topic == 'piv/device1/cmnd/switch3':
        if msg == 'on':
            s3.set_on()
        else:
            s3.set_off()

client.set_callback(sub_cb)
client.set_last_will('piv/device1/stat/availability', 'offline', retain=True)
client.connect()
client.subscribe("piv/device1/cmnd/#")
client.publish('piv/device1/stat/availability', 'online', retain=True)

while (not btnC.wasPressed()):
    client.check_msg()    
    wait(1)
    
client.disconnect()