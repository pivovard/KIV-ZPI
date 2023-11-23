from m5stack import *
from m5stack_ui import *
from uiflow import *
from machine import Pin, DAC, PWM

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


led = machine.Pin(27, machine.Pin.OUT)
btn = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)

led.value(1)

dac = DAC(Pin(26))
dac.write(180)

pwm = PWM(Pin(27), freq=20000, duty=50) #freq=100 bude blikat

count = 0
val = 0
i = 180
j = 50

while(not btnC.wasPressed()):
  if val != btn.value() and btn.value():
    count +=1
    
  lcd.clear()
  lcd.print(count)
  
  val = btn.value()
  led.value(not val)
  
  i+=10
  if i > 255:
    i = 180
  dac.write(i)
  
  j+=5
  if j > 100:
    j = 50
  pwm.duty(j)
  
  wait(0.2)




