#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
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
    file = open("characteristics1.mfd","wb+")
    print("CANTIDAD CARACTERISTICAS: " + str(len(f.downloadCharacteristics(0x01))))

    ##LOOP
    inverso = f.downloadCharacteristics(0x01)
    inverso.reverse()
    cantidadHastaCero = 0
    flag = 0
    for i in inverso:
	if(i==0):
		if(flag == 0):
			cantidadHastaCero+=1
	else:
		flag = 1	
    cantidadHastaCero = 512-cantidadHastaCero
    counter = 0
    counterbloque = 0
    ##hasta aca era para que deje de meter ceros


    ## primer bloque
    while(counterbloque < 48):
	file.write('\x00')
	counterbloque+=1
	

    ## resto de bloques
    ## preparo cadena
    lista = []
    for i in f.downloadCharacteristics(0x01):
	if(cantidadHastaCero>counter):
		a = str(hex(i))[2:]
		for j in a:
		    lista.append(j)
		    counter+=1
    counter=0
    countertotal = 0	
    counteravance = 0
    print("tamano " + str(len(lista)))
    for i in lista:
        if(counteravance>=64):
            counteravance = 0
	while(counteravance<16):
	    file.write('\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x07\x80\x69\x00\x00\x00\x00\x00\x00')
	    countertotal+=16
	    counteravance+=16
	file.write(i)
        file.write('\x00')
	countertotal+=2
	counteravance+=2
    
    while(countertotal < 965):
        if(counteravance>=64):
            counteravance = 0
	while(counteravance<16):
	    file.write('\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x07\x80\x69\x00\x00\x00\x00\x00\x00')
	    countertotal+=16
	    counteravance+=16
	if(countertotal < 965):
		file.write('\x00')
	countertotal+=1
	counteravance+=1

    print(str(countertotal))
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
########################################################################    
 
except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)






















	
