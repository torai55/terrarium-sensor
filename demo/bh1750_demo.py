import RPi.GPIO as GPIO
import smbus2
import time

class MainApp:
    def __init__(self) -> None:
        self.light_mod = Light_Mod_Manager()
    def run(self):
        try:
            self.light_mod.loop()
        except KeyboardInterrupt:
            self.destroy()
    def destroy():
        GPIO.cleanup()

class Light_Mod_Manager:
    def __init__(self) -> None:
        # 預設 I2C 位址
        # ADDR 腳位在低電位時是 0x23
        # 高電位時是 0x5C
        self.DEVICE      = 0x23
        # 關閉電源
        self.POWER_DOWN  = 0x00
        # 打開電源
        self.POWER_ON    = 0x01
        # Reset Data register value. Reset command is not acceptable in Power Down mode.
        self.RESET       = 0x07

        # resolution 4 lx, 16 ms measurement time
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        # resolution 1 lx, 120 ms measurement time
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        # resolution 0.5 lx, 120 ms measurement time
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        # resolution 0.5 lx, 120 ms measurement time
        # automatically set to Power Down mode after measurement
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        # resolution 0.5 lx, 120 ms measurement time
        # automatically set to Power Down mode after measurement
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        # resolution 1 lx, 120 ms measurement time
        # automatically set to Power Down mode after measurement
        self.ONE_TIME_LOW_RES_MODE = 0x23
        if (GPIO.RPI_REVISION == 1):
            self.bus = smbus2.SMBus(0) # Rev 1 Pi uses 0
        else:
            self.bus = smbus2.SMBus(1) # Rev 2 Pi uses 1
    def convertToNumber(self,data):
    # 感測器採取 Big-Endian，最高有效位數放在記憶體最低位 data[0]
    # 將高位數字乘以 256，可以當作位元運算，將高位數左移八位
    # 除以 1.2 是感測器設定的 Measurement Accuracy
    # 若使用解析度為 0.5 lx 的模式
    # 最低有效位數代表的是 2^-1，算法就會不一樣
        result = (data[1] + (256 * data[0])) / 1.2
        return(result)

    def readLight(self, addr = None):
        if addr is None:
            addr = self.DEVICE
        data = self.bus.read_i2c_block_data(addr, self.ONE_TIME_HIGH_RES_MODE_1, 16)
        return self.convertToNumber(data)

    def loop(self):
        while True:
            lightLevel = self.readLight()
            print("BH1750 Light Level :" + format(lightLevel, '.2f') + "lx")
            time.sleep(2)

if __name__ == "__main__":
    app = MainApp()
    app.run()
