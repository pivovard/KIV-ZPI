from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

btn = M5Btn("Play", x=15, y=15, w=50, h=30)
ch = M5Checkbox("Checkbox", x=15, y=50, w=50, h=30, text_c=0x0288FB, check_c=0xCCCCCC)
switch = M5Switch(x=15, y=85, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB)
slider = M5Slider(15,120,100,30, 0,100)

def pressed_cb():
    lcd.print("btn was pressed ")
    switch.set_on()
    a = slider.get_value()
    slider.set_value(a+10)
    
    power.setVibrationEnable(True)
    wait(2)
    power.setVibrationEnable(False)
    speaker.playTone(131, 1)
    
def swon():
  lcd.print("Switch on")
  
def onChange(value):
  lcd.print("Slider value: ")
  lcd.print(value)

btn.pressed(pressed_cb)
switch.on(swon)
slider.changed(onChange)

while(not btnC.wasPressed()):
  wait(0.2)