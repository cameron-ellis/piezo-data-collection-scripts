import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ssd1306
from adafruit_ads1x15.analog_in import AnalogIn

# Define reset pin for display
oled_reset = digitalio.DigitalInOut(board.D4)

# Display dimensions
WIDTH = 128
HEIGHT = 64

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
# ads = ADS.ADS1115(i2c)

# Create instance of SSD1306 I2C Driver
oled = adafruit_ssd1306.SSD1306_I2C(
    WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear Display
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
# draw.rectangle(
# (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
# outline=0,
# fill=0,
# )

# Load default font.
# font = ImageFont.load_default()

# Draw Some Text
# text = "Hello World!"
# (font_width, font_height) = font.getsize(text)
# draw.text(
# (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
# text,
# font=font,
# fill=255,
# )

# Display image
# oled.image(image)
# oled.show()

# Create single-ended input on channel 0
# chan = AnalogIn(ads, ADS.P0)

# while True:
# print("CHAN 0: "+"{:>5.6f} V".format(chan.voltage))
# time.sleep(0.5)
