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
            prev_time = curr_time
        except KeyboardInterrupt:
            print('\nExit\n')
            break
