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
        
        sensorValue = 0 
        P= 0
        
        
        for x in range(0, 100):
            sensorValue = sensorValue + adc.read_voltage(1)
         #get average of reading
        sensorValue = sensorValue/100.0       
        P = ((sensorValue/3.0)-0.04)/0.018
        print("sensorValue: %02f" % sensorValue )
        print("Pressao: %02f" % P )
        time.sleep(3)
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    main()
