import time
import display_test
import adc_test
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn

# Variable for previous voltage and time
prev_vmeas = 0.0
prev_time = 0.0

# Loop that constantly reads and updates display
while True:
    try:
        display_test.clear_screen()
        curr_time = time.time_ns()
        curr_vmeas = adc_test.voltage_read()
        curr_imeas = adc_test.current_read(
            prev_vmeas, curr_vmeas, prev_time, curr_time)
        display_test.IV_disp(curr_vmeas, curr_imeas)
        prev_vmeas = curr_vmeas
        prev_time = curr_time
        time.sleep(0.5)
    except KeyboardInterrupt:
        display_test.clear_screen()
        display_test.exit_disp()
        time.sleep(3)
        display_test.clear_screen()
        print('\nExit\n')
        break
