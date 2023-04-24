import time
import display_test
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn

# Constants for conversion
pico_farad = (100*(10**(-12)))  # constant for 100 pF capacitor
ns_to_sec = (10**(-9))  # constant for nanoseconds to seconds
a_to_na = (10**9)  # constant for amps to nanoamps

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0 for voltage measurement
v_meas = AnalogIn(ads, ADS.P0)


def voltage_read():
    # Read voltage from Channel 0
    actual_voltage = (((v_meas.voltage*(5/3.3))-0.3817)/8.3867)
    # Return actual voltage after calculating voltage division
    return actual_voltage


def current_read(prev_v, curr_v, prev_t, curr_t):
    delta_v = curr_v - prev_v
    delta_t = (curr_t - prev_t)*(ns_to_sec)
    calc_current = ((pico_farad)*(delta_v)/(delta_t))*(a_to_na)
    # Return calculated current from differential voltage over time
    return calc_current
