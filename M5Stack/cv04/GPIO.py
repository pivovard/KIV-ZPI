from m5stack import *
from m5stack_ui import *
from uiflow import *
from machine import Pin


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

pinOUT = machine.Pin(27, machine.Pin.OUT)
pinIN = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)

count = 0
value = 1

while(not btnC.wasPressed()):
  val = pinIN.value()
  if val != value and val == 0:
    count +=1
    
  value = val
  pinOUT.value(not val)
  
  lcd.clear()
  lcd.print('Pressed: %d' % int(not val),0,0)
  lcd.print('Count: %d' % count,0,15)
  
  wait(0.2)

lcd.clear()
lcd.print('Finnished.',0,0)