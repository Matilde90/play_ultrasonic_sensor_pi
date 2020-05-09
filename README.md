# Sound of distance - using ultrasonic sensor

## Summary

This project consists in the sonification of distance of a surface from an ultrasonic sensor. Distance data is then transformed into an audible MIDI note which in turn is played by the Sonic-pi.
<br/>
![ultrasonic_sensor_image](ultrasonic_sensor.jpg)

## Description

This project was inspired from [this tutorial](https://projects.raspberrypi.org/en/projects/ultrasonic-theremin).

The ultrasonic sensor is plugged into the Raspberry pi ports and receives 5V power supply. The output signal needs to be converted to 3.3v to not damage the Raspberry pi. For this, I built a voltage divider circuit (see picture above).

A useful tutorial on how to assemble the circuit and a slightly different architecture of voltage dividers could be found [here](https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi).

For this project I used the ultrasonic sensor to obtain information about the distance of an object from the sensor. I then mapped this information into a playable MIDI note, and send this information to Sonic-pi. 

As Sonic-pi listens on port 4560, I used the python-osc library to send MIDI data to the sonic-pi. The documentation on receiving OSC messages could be found [here](https://github.com/samaaron/sonic-pi/blob/master/etc/doc/tutorial/12.1-Receiving-OSC.md).

### Used hardware
1. Breadboard
2. 3 x  1 Ohm resistor, 1 x 0 Ohm resistor
3. HC-SRO4 ultrasonic sensor 
4. Raspberry pi power supply
5. Dupont wires
6. Optional: base for holding your ultrasonic sensor - I recycled an used pepper container and covered it with papier-mâché

#### Useful commands to work with the raspberry pi:

- I found useful to work entirely from my laptop, enabling an ssh connection to comunicate to the raspberry pi. Once the ssh connection is enabled, I copy data from my computer to the raspberry pi via the scp command.

```bash
scp -i ~/.ssh/<your-raspberry-pi-private-key>  \
     <path-to-the-origin-file> \
    pi@<ip-of-the-pi>:<path-to-the-destination-folder>
```

## Acknowledgments

Thank you very much to Auro Michele Perego for invaluable suggestions on voltage dividers and scaling techniques. 
 