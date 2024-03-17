# Gas Detection, written by Theocharis Anastopoulos, 2023

# importing libraries 
# MQ2 sensor
    # Ported from https://github.com/amperka/TroykaMQ
    # Author: Alexey Tveritinov [kartun@yandex.ru]
#I2C_LCD_driver
    ## Original code found at:
    # https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
    # By DenisFromHR (Denis Pleic)
from mq2 import MQ2
import I2C_LCD_driver
import utime
from machine import Pin
import _thread

# Buzzer, goes On when detects Gas
buzzer = machine.Pin(14, machine.Pin.OUT)
buzzer_state = False  # Track the state of the buzzer

# Red Led, goes On when detects Gas
led = machine.Pin(15, machine.Pin.OUT)
led_state = False  # Track the state of the LED

# "Power On" LED
power_led = machine.Pin(16, machine.Pin.OUT)
power_led.on()  # Turn on the power LED initially

# LCD
lcd = I2C_LCD_driver.lcd()
# MQ2 sensor
pin = 27
sensor = MQ2(pinData=pin, baseVoltage=5)
print("Starting...")
sensor.calibrate()
print("Resistance:{0}".format(sensor._ro))
lcd.lcd_clear()
lcd.lcd_display_string("Starting...")

# MQ2 sensor is able to detect
# LPG, i-butane, propane, methane, alcohol, Hydrogen, smoke
# We have a 16x2 LCD, so we will use Smoke and Methane Detection only
state = {'buzzer_state': False, 'led_state': False}  # Create a state dictionary

def buzzer_thread(state):
    log_file = open("gas_detection_log.txt", "a")  # Open the log file in append mode
    while True:
        smoke = sensor.readSmoke()
        methane = sensor.readMethane()
        if float(smoke) > 50 or float(methane) > 50:
            if not state['buzzer_state']:
                buzzer.on()
                state['buzzer_state'] = True
            if not state['led_state']:
                led.on()
                state['led_state'] = True
        else:
            if state['buzzer_state']:
                buzzer.off()
                state['buzzer_state'] = False
            if state['led_state']:
                led.off()
                state['led_state'] = False
                utime.sleep(5)

_thread.start_new_thread(buzzer_thread, (state,))

while True:
    smoke = sensor.readSmoke()
    methane = sensor.readMethane()
    print("Measuring..")
    print("Smoke: {:.1f}".format(smoke)+" - ", end="")
    print("Methane: {:.1f}".format(methane)+" - ", end="")
    lcd.lcd_clear()
    lcd.lcd_display_string("Smoke: {:.1f}ppm".format(smoke), 1)
    lcd.lcd_display_string("Methane:{:.1f}ppm".format(methane), 2)
    utime.sleep(5)
