# Terrarium sensor

Using Raspberry Pi project for monitoring light, humidity, temperature.  
Upload data to [ThingSpeak](https://thingspeak.com/) to build chart.  

Device:

- Raspberry Pi Zero W
- GPIO Extension Board
- bh1750
- dht22
- 2004A lcd with PCF8574 adapter

For more detail, read [my blog](https://torai55.github.io/blog/posts/computer-science/terrarium-sensor-03/).  

## usage

Requires pre-installation of pyenv, poetry  

1. `$ pyenv install 3.10.10`
2. `$ pyenv local 3.10.10`
3. `$ poetry env use 3.10.10`
4. `$ poetry shell`
5. `$ poetry install`
6. `$ python main.py`
