import csv
import time
import adc_test
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn
import csv

# Variable for previous voltage and time
prev_vmeas = 0.0
prev_time = 0.0

# # Create I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)

# # Create the ADC object using the I2C bus
# ads = ADS.ADS1115(i2c)

# # Create single-ended input on channel 0 for voltage measurement
# v_meas = AnalogIn(ads, ADS.P0)

# # Create single-ended input on channel 1 for current measurement
# i_meas = AnalogIn(ads, ADS.P1)

with open('/tmp/IV_meas_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Voltage (V)", "Current (nA)"]
    writer.writerow(field)
    # Loop that constantly reads and updates display
    while True:
        try:
            curr_time = time.time_ns()
            curr_vmeas = adc_test.voltage_read()
            curr_imeas = adc_test.current_read(
                prev_vmeas, curr_vmeas, prev_time, curr_time)
            v_out = "{:>5.6f}".format(curr_vmeas)
            i_out = "{:>5.6f}".format(curr_imeas)
            IV_measurements = [v_out, i_out]
            writer.writerow(IV_measurements)
            prev_vmeas = curr_vmeas
            prev_time = time.time_ns()
        except KeyboardInterrupt:
            print('\nExit\n')
            break
    # while True:
    #     try:
    #         voltage = (((v_meas.voltage*(5/3.3))-0.3817)/8.3867)
    #         v_out = "{:>5.6f}".format(voltage)
    #         IV_measurements = [v_out]
    #         writer.writerow(IV_measurements)
    #     except KeyboardInterrupt:
    #         print('\nExit\n')
    #         break
