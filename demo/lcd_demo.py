from RPLCD.i2c import CharLCD
from time import sleep

cols = 20
rows = 4
charmap = "A00"
i2cExpander = "PCF8574"
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

lcd = CharLCD(i2cExpander, address, port=port,
    charmap=charmap, cols=cols, rows=rows)

lcd.write_string("Hello world")
lcd.crlf()
lcd.write_string("IoT with Torai")
lcd.crlf()
lcd.write_string("Raspberry pi")
sleep(5)
lcd.backlight_enabled = False 
lcd.close(clear=True)