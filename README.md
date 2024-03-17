```markdown
# Raspberry Pi Pico Gas Sensor Project

This project utilizes a Raspberry Pi Pico microcontroller to detect smoke and methane gas using an MQ2 sensor.
It includes integration with an LCD 16x02, a buzzer, and LEDs to indicate various states of the system.

## Components Used

- Raspberry Pi Pico
- MQ2 Gas Sensor
- LCD 16x02
- Buzzer
- LEDs (Green and Red)

## Wiring Guide

### LCD Wiring:

- GND --> PICO GND
- VCC --> PICO 40 (VBUS)
- SDA --> PICO 1 (GP0)
- SCL --> PICO 2 (GP1)

### MQ2 Sensor Wiring:

- VCC --> PICO 1 (VSYS)
- GND --> PICO 3 (GND)
- A.OUT --> PICO 10 (GP26)

### Buzzer Wiring:

- GND --> PICO 18 (GND)
- + --> PICO 19 (GP14)

### Green LED Wiring:

- + --> PICO 21 (GP16) (Use 220Ω-330Ω resistor in the positive lead)
- - --> PICO 23 (GND)

### Red LED Wiring:

- + --> PICO 20 (GP15) (Use 220Ω-330Ω resistor in the positive lead)
- - --> PICO 23 (GND)

## Functionality

- The system detects smoke and methane gas using the MQ2 sensor.
- When gas is detected, the buzzer beeps and the red LED lights up.
- A green LED indicates that the program is up and running.

## Usage

1. Clone the repository:

git clone https://github.com/theo79/raspberry_pico_sensors.git

    Upload the code to your Raspberry Pi Pico.
    Ensure the wiring is done correctly as per the provided guide.
    Power on the Raspberry Pi Pico.
    Observe the behavior of the system based on the presence of gas.

##Notes

The MQ2 sensor can detect more gases than smoke and methane, but only these two are displayed due to the limitations of the LCD 16x02.

Feel free to contribute or provide feedback on this project!
