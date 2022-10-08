#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import binascii
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

BLOCK_SIZE	= 48


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
    

    datosUser = "Juan Francisco;Miguez;1045062;38844261;10/11/2019;"
    print("Bytes del usuario: " + str(len(datosUser)))
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## GUARDAR HUELLA EN characteristics1.
        ## Subimos string al buffer 1.
    f.convertImage(0x01)
    print("CANTIDAD CARACTERISTICAS: " + str(len(f.downloadCharacteristics(0x01))))



    ## EXTRACCION DE PLANTILLA DE LA TARJETA
    os.system("nfc-mfclassic r a rawcard.mfd")
    reader = open("rawcard.mfd", "rb")
    file = open("processed.mfd", "wb")
    

    ## CUANTOS CEROS
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
    
    ## GRABAR DATOS TARJETA
    
    reader.seek(0,0)
    crudo= reader.read(48)
    file.write(crudo)
    counterbloque+=48
    
    # GRABAR DATOS USUARIO (sin solapar llaves).
    file.seek(64, 0)
    
    counter=0
    userDataList = []
    userDataList [:0] = datosUser

    for i in userDataList:
        if (counter > BLOCK_SIZE-1):
	    file.seek(16, 1)
	    counter=0
	file.write(i)
	counter+=1
    
    # GRABAR DATOS HUELLA (sin solapar llaves).
    counterCero = 0
    for i in f.downloadCharacteristics(0x01):
	if(counterCero < cantidadHastaCero):

	    for j in str(i):
                if (counter > BLOCK_SIZE-1):
	            file.seek(16, 1)
	            counter=0
	        file.write(str(j))
	        counter += len(str(j))
		counterCero += len(str(j))

            if (counter > BLOCK_SIZE-1):
	        file.seek(16, 1)
	        counter=0
            file.write('\x00')
	    counter += len('\x00')
	    counterCero += len('\x00')
	

    # GRABAR DATOS LLAVES.
    reader.seek(0,0)
    file.seek(0,0)
    countertotal=0
    while(countertotal < 965):
	reader.seek(48, 1)
    	crudo= reader.read(16)
	file.seek(48, 1)
    	file.write(crudo)
	
        countertotal+=64

    # GENERAR EL HASH DE TODO LO ANTERIOR

	#los datos del usuario y la huella crudos.
        #la estructura de la huella es [a,b,c,d,e,f]
    sinPicar = datosUser + str(f.downloadCharacteristics(0x01))
    picadillo = hashlib.sha224(sinPicar).hexdigest()
    print(sinPicar)
    print(picadillo)


    # FIRMAR EL HASH (picadillo)


    with open("privateKey", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    message = picadillo
    signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    file = open(message+"FIRMADO", "wb")
    file.write(signature)
    file.close
    
    
    file.close()
    reader.close()
    ## LEVANTAR HUELLA DE characteristics2.
    #file = open("characteristics2", "r")
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






















	
