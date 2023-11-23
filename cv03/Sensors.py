from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit
import imu

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x0)

sensor_type = 'ENV2'

if sensor_type == 'ANGLE':
  angle = unit.get(unit.ANGLE, unit.PORTA)
if sensor_type == 'SONIC':
  ultrasonic = unit.get(unit.ULTRASONIC, unit.PORTA)
if sensor_type == 'ENV2':
  env = unit.get(unit.ENV2, unit.PORTA)
if sensor_type == 'GESTURE':
  sensor = unit.get(unit.GESTURE, unit.PORTA)
  sensor.begin()
  
imu0 = imu.IMU()

while not btnC.wasPressed():
  lcd.clear()
  
  if sensor_type == 'ANGLE':
    lcd.print(angle.read(),0,0)
  if sensor_type == 'SONIC':
    lcd.print('%f mm' % ultrasonic.distance,0,0)
  if sensor_type == 'ENV2':
    lcd.print('Temperature: %f' % env.temperature, 0,0)
    lcd.print('Pressure:    %f' % env.pressure, 0,15)
    lcd.print('Humidity:    %f' % env.humidity, 0,30)
  if sensor_type == 'GESTURE':
    lcd.print('%s' % sensor.get_gesture,0,0)
    
  lcd.print('Acc:  %f %f %f' % (imu0.acceleration[0], imu0.acceleration[1], imu0.acceleration[2]), 0,50)
  lcd.print('Gyro:  %f %f %f' % (imu0.gyro[0], imu0.gyro[1], imu0.gyro[2]), 0,80)
  
  wait(0.5)