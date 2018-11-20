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



def mapi(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;


def main():
    '''
    Main program function
    '''

    adc = ADCPi(0x68, 0x69, 12)
    
    res = 10000
    termres = 10000
    tempnominal = 25
    beta = 3977

    
    while True:

        # clear the console
        os.system('clear')
        
        sensorValue = 0 ;  
        
        for x in range(0, 100):
            sensorValue = sensorValue + adc.read_voltage(1)
         #get average of reading
        sensorValue = sensorValue/100.0       
        media = sensorValue - 1
        media = res / media
        temperatura = media / termres
        temperatura = math.log(temperatura)
        temperatura /= beta
        temperatura += 1.0 / (tempnominal + 273.15)
        temperatura = 1.0 / temperatura
        temperatura -= 273.15
        print("media: %02f" % temperatura )
        time.sleep(3)
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    main()
