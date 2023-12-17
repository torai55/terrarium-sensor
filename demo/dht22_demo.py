from time import sleep
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D6)

while True:
    try:
        # Print the values to the serial port
        temperatureC = dhtDevice.temperature
        temperatureF = temperatureC * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperatureF, temperatureC, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    sleep(2.0)
