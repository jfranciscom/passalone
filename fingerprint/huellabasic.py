#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)
##########################################################################################################################

try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## GUARDAR HUELLA EN characteristics1.
        ## Subimos string al buffer 1.
    f.convertImage(0x01)
    file = open("characteristicsBasic","w+")
    file.write(str(f.downloadCharacteristics(0x01)).replace('[', '').replace(']', ''))
    file.close()
    
    ## LEVANTAR HUELLA DE characteristics2.
    file = open("characteristics2", "r")
        ## Procesamos el string.        
    caract2 = map(int, file.read().split(', '))
        ## Subimos el string al buffer 2.
    f.uploadCharacteristics(0x02, caract2)

    if ( f.compareCharacteristics() == 0 ):
        print("NO COINCIDEN.")
    else:
        print("SI COINCIDEN.")
    
  
    print("Todo salio bien.")
   
except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
