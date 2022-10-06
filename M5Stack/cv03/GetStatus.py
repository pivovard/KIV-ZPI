from m5stack import *
from m5stack_ui import *
from uiflow import *
from easyIO import *


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

lBat = M5Label('Bat', x=250, y=15, color=0xFFFFFF, font=FONT_MONT_14, parent=None)
lTime = M5Label('Time', x=15, y=15, color=0xFFFFFF, font=FONT_MONT_14, parent=None)
lTouch = M5Label('X: 0, Y: 0', x=15, y=50, color=0xFFFFFF, font=FONT_MONT_14, parent=None)
switch = M5Switch(x=15, y=85, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)

rtc.settime('ntp', host='cn.pool.ntp.org', tzone=1)


while(True):
  bat = map_value((power.getBatVoltage()), 3.7, 4.1, 0, 100)
  lBat.set_text("%d%%" % bat)
  
  time = rtc.datetime()
  lTime.set_text("%d-%d-%d %d:%d:%d" % (time[0], time[1], time[2], time[4], time[5], time[6]))
  
  t = touch.read()
  lTouch.set_text("X: %d, Y: %d" % (t[0], t[1]))
  
  wait(0.2)