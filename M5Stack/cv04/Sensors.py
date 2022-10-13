from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

# angle_0 = unit.get(unit.ANGLE, unit.PORTA)

# while not btnC.wasPressed():
#   lcd.clear()
#   lcd.print(angle_0.read(),0,0)
#   wait(0.2)

env_0 = unit.get(unit.ENV2, unit.PORTA)
lcd.print('test')
wait(5)

lcd.clear()
lcd.print('Temp: %f' % env_0.temperature, 0,0)
lcd.print('Temp: %f' % env_0.pressure, 0,15)
lcd.print('Temp: %f' % env_0.humidity, 0,30)

  
lcd.clear()
lcd.print('Finnished.',0,0)