import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn

# Define reset pin for display
# oled_reset = digitalio.DigitalInOut(board.D4)

# Display dimensions
WIDTH = 128
HEIGHT = 64

# Create I2C bus
i2c = board.I2C()
# Create instance of SSD1306 I2C Driver
oled = adafruit_ssd1306.SSD1306_I2C(
    WIDTH, HEIGHT, i2c, addr=0x3d)

# Clear Display
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()


def clear_screen():
    # Clear Display
    oled.fill(0)
    oled.show()
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Load default font.
    font = ImageFont.load_default()
    # Draw a white background
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)


def IV_disp(v_meas, i_meas):
    # Clear Display
    oled.fill(0)
    oled.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Load default font.
    font = ImageFont.load_default()
    # Display values for
    voltage = "V: "+"{:>5.6f} V".format(v_meas)
    current = "I: "+"{:>5.6f} A".format(i_meas)
    draw.text(
        (15, 20),
        voltage,
        font=font,
        fill=255,
    )
    draw.text(
        (15, 35),
        current,
        font=font,
        fill=255,
    )
    # Display image
    oled.image(image)
    oled.show()
