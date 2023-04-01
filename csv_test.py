import csv
import time
import display_test
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn
import csv

# Voltage offset input to instrumentation amplifier for current measurement
# v_offset = 1

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0 for voltage measurement
v_meas = AnalogIn(ads, ADS.P0)

# Create single-ended input on channel 1 for current measurement
i_meas = AnalogIn(ads, ADS.P1)

with open('/tmp/IV_meas_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Voltage (V)", "Current (A)"]
    writer.writerow(field)

    while True:
        try:
            voltage = "{:>5.6f}".format(v_meas.voltage)
            current = "{:>5.6f}".format(i_meas.voltage)
            IV_measurements = [voltage, current]
            writer.writerow(IV_measurements)
        except KeyboardInterrupt:
            print('\nExit\n')
            break
