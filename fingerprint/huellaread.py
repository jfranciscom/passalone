#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os
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
    


    ## LEVANTAR HUELLA DE characteristics2.
    file = open("characteristics1.mfd", "r")
    valores = []
    cadena = ""
    counter = 0
    countpartes = 0
    file.seek(64)
    try:
        while(counter<16):
	    cadena=""
	    while(countpartes < 48):
		letra = file.read(1)
            	cadena += letra
		if(letra == '\x00'):
		    valores.append(cadena)
		countpartes+=1
	    countpartes = 0
      	    file.seek(16, 1)
	    counter+=1
        print(valores)

    except Exception as e:
	print("Termina de leer")
        ## Procesamos el string.
        
    #caract2 = map(int, file.read().split(', '))
        ## Subimos el string al buffer 2.
    #f.uploadCharacteristics(0x02, caract2)

    #if ( f.compareCharacteristics() == 0 ):
    #    print("NO COINCIDEN.")
    #else:
    #    print("SI COINCIDEN.")
########################################################################    
 
except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)






















	
