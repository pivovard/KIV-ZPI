from m5stack import lcd, btnC

exit = False

def pressed():
    global exit
    exit = True
btnC.wasPressed(pressed)

while(True):
    if exit: break
    wait(1)

lcd.clear()
lcd.print('Finnished!', 0, 0)