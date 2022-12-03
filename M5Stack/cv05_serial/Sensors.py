from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

sensor_type = 'TEMP'

if sensor_type == 'ANGLE':
  angle = unit.get(unit.ANGLE, unit.PORTA)
if sensor_type == 'SONIC':
  ultrasonic = unit.get(unit.ULTRASONIC, unit.PORTA)
if sensor_type == 'TEMP':
  env = unit.get(unit.ENV2, unit.PORTA)

lcd.clear()


while not btnC.wasPressed():
  lcd.clear()
  
  if sensor_type == 'ANGLE':
    lcd.print(angle.read(),0,0)
  if sensor_type == 'SONIC':
    lcd.print('%f mm' % ultrasonic.distance,0,0)
  if sensor_type == 'TEMP':
    lcd.print('Temperature: %f' % env.temperature, 0,0)
    lcd.print('Pressure:    %f' % env.pressure, 0,15)
    lcd.print('Humidity:    %f' % env.humidity, 0,30)
  
  wait(0.5)