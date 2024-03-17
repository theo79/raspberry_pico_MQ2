<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>Raspberry Pi Pico Gas Sensor Project</h1>

<p>This project utilizes a Raspberry Pi Pico microcontroller to detect smoke and methane gas using an MQ2 sensor. It includes integration with an LCD 16x02, a buzzer, and LEDs to indicate various states of the system.</p>

<h2>Components Used</h2>
<ul>
    <li>Raspberry Pi Pico</li>
    <li>MQ2 Gas Sensor</li>
    <li>LCD 16x02</li>
    <li>Buzzer</li>
    <li>LEDs (Green and Red)</li>
</ul>

<h2>Wiring Guide</h2>

<h3>LCD Wiring:</h3>
<ul>
    <li>GND -&gt; PICO GND</li>
    <li>VCC -&gt; PICO 40 (VBUS)</li>
    <li>SDA -&gt; PICO 1 (GP0)</li>
    <li>SCL -&gt; PICO 2 (GP1)</li>
</ul>

<h3>MQ2 Sensor Wiring:</h3>
<ul>
    <li>VCC -&gt; PICO 1 (VSYS)</li>
    <li>GND -&gt; PICO 3 (GND)</li>
    <li>A.OUT -&gt; PICO 10 (GP26)</li>
</ul>

<h3>Buzzer Wiring:</h3>
<ul>
    <li>GND -&gt; PICO 18 (GND)</li>
    <li>+ -&gt; PICO 19 (GP14)</li>
</ul>

<h3>Green LED Wiring:</h3>
<ul>
    <li>+ -&gt; PICO 21 (GP16) (Use 220Ω-330Ω resistor in the positive lead)</li>
    <li>- -&gt; PICO 23 (GND)</li>
</ul>

<h3>Red LED Wiring:</h3>
<ul>
    <li>+ -&gt; PICO 20 (GP15) (Use 220Ω-330Ω resistor in the positive lead)</li>
    <li>- -&gt; PICO 23 (GND)</li>
</ul>

<h2>Functionality</h2>
<ul>
    <li>The system detects smoke and methane gas using the MQ2 sensor.</li>
    <li>When gas is detected, the buzzer beeps and the red LED lights up.</li>
    <li>A green LED indicates that the program is up and running.</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/theo79/raspberry_pico_sensors.git
</code></pre>

<ol start="2">
    <li>Upload the code to your Raspberry Pi Pico.</li>
    <li>Ensure the wiring is done correctly as per the provided guide.</li>
    <li>Power on the Raspberry Pi Pico.</li>
    <li>Observe the behavior of the system based on the presence of gas.</li>
</ol>

<h2>Note</h2>
<ul>
    <li>The MQ2 sensor can detect more gases than smoke and methane, but only these two are displayed due to the limitations of the LCD 16x02.</li>
</ul>

<p>Feel free to contribute or provide feedback on this project!</p>

</body>
</html>

