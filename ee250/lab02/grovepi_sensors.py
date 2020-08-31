""" EE 250L Lab 02: GrovePi Sensors
By: Zechen Wang

Insert Github repository link here.
https://github.com/ZechenWangUSC/GrovePi-EE250
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
    lcd.setRGB(153,255,51)

    grovepi.pinMode(meter, "INPUT")

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        deg = round( grovepi.analogRead(meter) * 300 / 1023) #range: [0,300]
        print("Rot Sensor:" + str(deg))

        dist = grovepi.ultrasonicRead(PORT)
        print("Distance:" + str(dist))
        
        if dist < deg:
            lcd.setText_norefresh("%3dcm OBJ PRES\n%3dcm" % (deg,dist))
        else:
            lcd.setText_norefresh("%3dcm          \n%3dcm" % (deg,dist))
