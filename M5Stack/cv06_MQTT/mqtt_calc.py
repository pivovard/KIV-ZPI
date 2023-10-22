from m5stack import *
from m5stack_ui import *
from umqttsimple import MQTTClient
import ubinascii
import machine
import network
import gc
import random

gc.collect()
lcd.clear()

ssid = 'ssid'
password = 'pass'

mqtt_server = 'test.mosquitto.org'
client_id = ubinascii.hexlify(machine.unique_id())

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

def sub_cb(topic, msg):
    print((topic, msg))
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
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server,1883)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe('zpi/math')
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
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

# mosquitto_sub -t "zpi/res" -v -h test.mosquitto.org
# mosquitto_pub -t 'test/topic' -m 'hello world' -h test.mosquitto.org
