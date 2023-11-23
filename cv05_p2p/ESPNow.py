from m5stack import *
from m5ui import *
import espnow, wifiCfg

setScreenColor(0x000000)

wifiCfg.wlan_ap.active(True)
wifiCfg.wlan_sta.active(True)

espnow.init(0)
addr = espnow.get_mac_addr()

espnow.add_peer('30aea4587df1', id=1)

title = M5Title(title=addr, x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label = M5TextBox(10, 50, "Text", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label_s = M5TextBox(10, 100, "", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

def recv_cb(_):
  addr, _, data = espnow.recv_data(encoder='str')
  label.setText(data)
  label_s.setText(data)
espnow.recv_cb(recv_cb)

def send_cb(flag):
  if flag:
    label.setText('succeed')
  else:
    label.setText('Failed')
espnow.send_cb(send_cb)

def buttonA_wasPressed():
  espnow.send(id=1, data=str('Hello device!'))
  label.setText('sending')
btnA.wasPressed(buttonA_wasPressed)

espnow.broadcast(data='Hello World')
