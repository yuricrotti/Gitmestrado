#!/usr/bin/env python
"""
================================================
ABElectronics ADC Pi 8-Channel ADC demo

Requires python smbus to be installed
run with: python demo_readvoltage.py
================================================

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers

Sample rate can be 12,14, 16 or 18
"""

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time
import os

try:
    from ADCPi import ADCPi
except ImportError:
    print("Failed to import ADCPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCPi import ADCPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


def main():
    '''
    Main program function
    '''

    adc = ADCPi(0x68, 0x69, 12)

    while True:

        # clear the console
        os.system('clear')
        
        sensor_volt = 0
        #Get the value of RS via in a clear air
        RS = 0 
        #Get the value of R0 via in Alcohol    
        R0  = 0
        sensorValue =0 
        
        #
        for x in range(0, 100):
            sensorValue = sensorValue + adc.read_voltage(1)
      
        #get average of reading
        sensorValue = sensorValue/100.0     
        sensor_volt = sensorValue
        RS = (5.0-sensor_volt)/sensor_volt
        
        # 60 is found using interpolation
        R0 = RS/60.0
        print("R0: %02f" % R0)
        print("sensor_volt: %02f" % sensor_volt)
           
        time.sleep(1)

if __name__ == "__main__":
    main()
