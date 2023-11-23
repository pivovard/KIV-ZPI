from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
from m5mqtt import M5mqtt

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x222222)

wifiCfg.doConnect('zpikiv', '78086975')

def sub_cb(topic_data):
  lcd.print(topic_data)
  pass

m5mqtt = M5mqtt('2', 'test.mosquitto.org', 1883, '', '', 0)
m5mqtt.subscribe(str('zpitest'), sub_cb)
m5mqtt.set_last_will('zpistatus', 'offline')
m5mqtt.start()
m5mqtt.publish(str('zpitest'), str('t'), )

wait(2)
m5mqtt.deinit()

# mosquitto_sub -t "zpitest" -v -h test.mosquitto.org
# mosquitto_pub -t "zpitest" -m "hello" -h test.mosquitto.org -r