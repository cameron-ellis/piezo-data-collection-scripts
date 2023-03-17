import time
import display_test
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn

# Voltage offset input to instrumentation amplifier for current measurement
v_offset = 1

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0 for voltage measurement
v_meas = AnalogIn(ads, ADS.P0)

# Create single-ended input on channel 1 for current measurement
i_meas = AnalogIn(ads, ADS.P1)

while True:
    try:
        display_test.clear_screen()
        calc_current = i_meas.voltage - v_offset
        display_test.IV_disp(v_meas.voltage, calc_current)
        time.sleep(0.5)
    except KeyboardInterrupt:
        display_test.clear_screen()
        print("Exit\n")
        break
