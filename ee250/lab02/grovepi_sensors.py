""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    meter = 0   # A0
    lcd.setRGB(153,255,51)  #I love this color

    grovepi.pinMode(meter, "INPUT")

    adc_ref = 5
    grove_vcc = 5
    max_angle = 300


    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        #ref: grove_rotary_angle_sensor.py
        val = grovepi.analogRead(meter)
        voltage = round( (float)(val) * adc_ref / 1023, 2)
        deg = round( (voltage * max_angle) / grove_vcc, 2)
        print("degrees:" + str(deg))

        dist = grovepi.ultrasonicRead(PORT)
        print("Distance:" + str(dist)
        lcd.setText_norefresh("%3dcm\n%3dcm" % (val,dist))
