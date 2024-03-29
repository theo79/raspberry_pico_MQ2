![Raspberry Pi Pico Gas Sensor Project](rpi_pico.jpg)

# Raspberry Pi Pico Gas Sensor Project

This project utilizes a Raspberry Pi Pico microcontroller to detect smoke and methane gas using an MQ2 sensor. It includes integration with an LCD 16x02, a buzzer, and LEDs to indicate various states of the system.

**MQ2 sensor**  Ported from https://github.com/amperka/TroykaMQ
    
 Author: Alexey Tveritinov [kartun@yandex.ru]

**I2C_LCD_driver**
https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

By DenisFromHR (Denis Pleic)

### Components Used

* Raspberry Pi Pico

* MQ2 Gas Sensor

* LCD 16x02

* Buzzer

* LEDs (Green and Red)

## Functionality

The system detects smoke and methane gas using the MQ2 sensor.
When gas is detected, the buzzer beeps and the red LED lights up.
A green LED indicates that the program is up and running.

## Usage

Clone the repository:

```bash
    git clone https://github.com/theo79/raspberry_pico_sensors.git
```

Upload the code to your Raspberry Pi Pico.

Ensure the wiring is done correctly as per the provided guide 
**(check wiring.txt)**

Power on the Raspberry Pi Pico.

Observe the behavior of the system based on the presence of gas.

## Notes
The MQ2 sensor can detect more gases than smoke and methane, 
 
but only these two are displayed due to the limitations of the LCD 16x02.

**MQ2 sensor requires preheat time for better measurement-detection. Check datasheet.**

Feel free to contribute or provide feedback on this project!
