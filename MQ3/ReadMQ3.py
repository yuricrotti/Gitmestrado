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
        
        sensor_volt=0.0
        RS_gas = 0.0 
        ratio=0.0 
        BAC=0.0
        
      
        sensor_volt = adc.read_voltage(1)
        print("sensor_volt: %02f" % sensor_volt)
        #omit *RL
        RS_gas = (5.0-sensor_volt)/sensor_volt
        print("RS_gas: %02f" % sensor_volt)
        
        #ratio = RS/R0  
        ratio = RS_gas/0.008825
        print("ratio: %02f" % ratio)
        
        #*-Replace the name "R0" with the value of R0 in the demo of First Test -*/ 
        BAC = (0.1896*(ratio**2)) - (8.6178*ratio/10) + 1.0792 
        print("BAC: %02f" % BAC)
        BACgl = BAC*0.0001 
        print("BAC (g/dL): %02f" % BACgl)


        time.sleep(1)

if __name__ == "__main__":
    main()
