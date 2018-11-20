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
import math

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
        resistor_multiplier = 6.95225 # use 100K resistor in series with the input
        zero_offset = 0.887 # zero offset value from calibration data printout
        slope = 0.030 # 
        
        sensorValue = 0   
        sensorValue = adc.read_voltage(1) * resistor_multiplier
        humidity = (sensorValue - zero_offset) / slope
        print("sensorValue: %02f" % sensorValue)	
        print("Humidity on channel 1: %0.1f%%" % humidity)
        time.sleep(3)
        
        

        

if __name__ == "__main__":
    main()
