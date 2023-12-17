import os
from datetime import datetime
import requests
from dotenv import load_dotenv
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
from dht22 import Dht22
from bh1750 import Bh1750

cols = 20
rows = 4
charmap = 'A00'
i2cExpander = 'PCF8574'
lcdAddress = 0x27 
port = 1 # 0 on an older Raspberry Pi

load_dotenv()

class MainApp:
    def __init__(self) -> None:
        self.dht = Dht22()
        self.bh1750 = Bh1750()
        self.lcd = CharLCD(i2cExpander, lcdAddress, port=port,
            charmap=charmap, cols=cols, rows=rows)

    def run(self):
        try:
            dhtData = self.dht.read()
            lightLevel = self.bh1750.read()

            apiKey = os.getenv('THING_SPEAK_API_KEY')
            tempC = str(dhtData.temperatureC)
            tempF = str(dhtData.temperatureF)
            humidity = str(dhtData.humidity)
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(f"Temp: {tempF} F / {tempC} C    Humidity: {humidity}% \n")
            print(f"BH1750 Light Level: {lightLevel} lx \n")

            self.lcd.write_string(now)
            self.lcd.crlf()

            self.lcd.write_string(f"Temp: {tempC} C")
            self.lcd.crlf()

            self.lcd.write_string(f"Humidity: {humidity} %")
            self.lcd.crlf()

            self.lcd.write_string(f"Light: {lightLevel} Lux")
            self.lcd.crlf()

            requests.get(f"https://api.thingspeak.com/update?api_key={apiKey}&field1={tempC}&field2={humidity}&field3={lightLevel}")
        except KeyboardInterrupt:
            self.destroy()

    def destroy(self):
        GPIO.cleanup()

if __name__ == "__main__":
    app = MainApp()
    app.run()
    app.destroy()
