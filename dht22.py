from time import sleep
import board
import adafruit_dht

class Dht22:
  def __init__(self) -> None:
    self.dhtDevice = adafruit_dht.DHT22(board.D6)

  def read(self):
      while True:
          try:
              dhtData = DhtData(self.dhtDevice.temperature, self.dhtDevice.humidity)
              self.dhtDevice.exit()
              return dhtData

          except RuntimeError as error:
              print(error.args[0])
              sleep(2.0)
              continue

          except Exception as error:
              self.dhtDevice.exit()
              raise error

class DhtData:
   def __init__(self, temperatureC, humidity) -> None:
      self.temperatureC = round(temperatureC, 1)
      self.temperatureF = round(temperatureC * (9 / 5) + 32, 1)
      self.humidity = round(humidity, 1)
