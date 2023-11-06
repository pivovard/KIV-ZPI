from m5stack import *
from m5stack_ui import *
import wifiCfg
from m5mqtt import M5mqtt
import ubinascii
import machine
import gc
import random

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x222222)

lcd.clear()

ssid = 'zpikiv'
password = '78086975'

mqtt_server = 'test.mosquitto.org'
client_id = ubinascii.hexlify(machine.unique_id())

wifiCfg.doConnect(ssid, password)

while True:
    if not (wifiCfg.wlan_sta.isconnected()):
        print("try reconnect")
        wifiCfg.reconnect()
print('Connection successful')
print(wifiCfg.wlan_sta.ifconfig())


def sub_cb(msg):
    client.publish('zpi/res', msg)

    input = msg.split()
    res = 0
    if input[2] == b'+':
        res = int(input[1]) + int(input[3])
    elif input[2] == b'-':
        res = int(input[1]) - int(input[3])
    elif input[2] == b'*':
        res = int(input[1]) * int(input[3])
    elif input[2] == b'/':
        res = int(input[1]) / int(input[3])

    msg = 'Name ' + str(input[0]) + ': ' + str(res)
    print(msg)
    client.publish('zpi/res', msg)

def connect_and_subscribe():
    global client_id, mqtt_server
    m5mqtt = M5mqtt(client_id, mqtt_server, 1883, '', '', 300)
    client.subscribe('zpi/math', sub_cb)
    client.start()
    print('Connected to %s MQTT broker, subscribed to %s topic' % mqtt_server)
    client.publish('zpi/test', 'Connected...')
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

counter = 0
while True:
    a = random.randrange(10000)
    b = random.randrange(10000)
    o = random.randrange(4)
    op = None
    res = 0
    if o == 0:
        op = '+'
        res = a+b
    elif o == 1:
        op = '-'
        res = a-b
    elif o == 2:
        op = '*'
        res = a*b
    else:
        op = '/'
        res = a/b

    msg = str(counter) + ' ' + str(a) + ' ' + op + ' ' + str(b)
    print(msg + ' = ' + str(res))
    client.publish('zpi/math', msg)

    client.check_msg()

    counter += 1
    wait(5)
