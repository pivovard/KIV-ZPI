from m5stack import lcd, btnC

while(not btnC.wasPressed()):
    lcd.print('Processing...', 0, 0)
    wait(1)

lcd.clear()
lcd.print('Finnished!', 0, 0)