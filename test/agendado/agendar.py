#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import binascii
import time
import os
from pyfingerprint.pyfingerprint import PyFingerprint
from copy import deepcopy
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

KEYS_SIZE		= 16
DATA_BLOCK_SIZE		= 48
ENTIRE_BLOCK_SIZE	= 64
BIOMETRIC_SIZE		= 256
POS_CHARACTS		= 320
POS_SIGN		= 672
POS_SEPARATOR		= 656


#########################################################################################################################
## Probamos disponibilidad de la huella.
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
    

    datosUser = "Juan Francisco;Miguez;1045062;38844261"
    fechaVenc = "10/11/2019"
    datosUser = "[" + datosUser + "][" + fechaVenc + "]"


    #print("Bytes del usuario: " + str(len(datosUser)))
    print('INGRESE SU HUELLA...')
 
    # Genero archivo para almacenar huella.
    fhuella = open("huella", "wt")
    fhuella.write(str(f.downloadCharacteristics(0x01)))
    fhuella.close()

    ## LECTURA DE HUELLA
    while ( f.readImage() == False ):
	pass
	

    ## GUARDAR HUELLA EN characteristics1.
        ## Subimos string al buffer 1.
    f.convertImage(0x01)




    ## EXTRACCION DE PLANTILLA DE LA TARJETA.
    os.system("nfc-mfclassic r a rawcard.mfd >> logs.txt")

    ## PREPARO FICHEROS DE ALMACENAMIENTO.
    reader = open("rawcard.mfd", "rb") # Lo que la tarjeta tenia.
    file = open("processed.mfd", "wb") # Lo que la tarjeta va a terminar teniendo.
    

    ## GRABAR DATOS NATIVOS DE LA TARJETA VIEJA EN LA NUEVA (no llaves).
    counterbloque = 0
    reader.seek(0,0)
    crudo= reader.read(DATA_BLOCK_SIZE)
    file.write(crudo)
    counterbloque+=DATA_BLOCK_SIZE
    
    # GRABAR DATOS USUARIO (sin solapar llaves).
    file.seek(ENTIRE_BLOCK_SIZE, 0)
    
    counter=0
    userDataList = []
    userDataList [:0] = datosUser

    for i in userDataList:
        if (counter > DATA_BLOCK_SIZE-1):
	    file.seek(KEYS_SIZE, 1)
	    counter=0
	file.write(i)
	counter+=1
    
    # GRABAR DATOS CARACTERISTICAS (sin solapar llaves).
    # Posicion inicial 320 = h140.
    # Le doy 256B a la huella, sino se repite. [P(X>256)=0.0031357]
    
    counterCero = 0 # Compresion.
    counter = 0 # Prevenir solapamiento de llaves.
    
    caracteristicas = []
    fhuella = open("huella", "rt")
    values = str(fhuella.read()).split('[')[1].split(']')[0].split(', ')
    for i in values:
	#print i
        caracteristicas.append(int(i))
    fhuella.close()
    

    file.seek(POS_CHARACTS, 0)
    #print(str(caracteristicas))
    
    for i in caracteristicas:
        #Agregado de datos.
	if (counter > DATA_BLOCK_SIZE-1):
	    file.seek(KEYS_SIZE, 1)
	    counter=0
	#print(str(i))
	file.write(chr(i))
        counter += 1
	counterCero += 1
    
    

    # AGREGO UN SEPARADOR DE "#"
    
    file.seek(POS_SEPARATOR, 0)
    for i in "################":
        if (counter > DATA_BLOCK_SIZE-1):
	    file.seek(KEYS_SIZE, 1)
	    counter=0
	file.write(i)
	counter+=1

    # GENERAR EL HASH DE TODO LO ANTERIOR

	#los datos del usuario y la huella crudos.
        #la estructura de la huella es [a,b,c,d,e,f]
    sinPicar = datosUser + str(caracteristicas)
    picadillo = hashlib.sha224(sinPicar).hexdigest()
    #print
    #print
    #print("SIN PICAR" + sinPicar)
    #print(picadillo)

    
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
    archsign = open("FIRMADO", "wb")
    #print("FIRMA: " + str(signature))
    #print("TAMANIO DE FIRMA: " + str(len(signature)))
    archsign.write(signature)
    archsign.close
    

    # GRABAR FIRMA DIGITAL.
    # Posicion inicial 2a0 = 672

    archsign = open("FIRMADO", "rb")
    file.seek(POS_SIGN, 0)

    counter = 32 # Ubicacion para sincronizado con las llaves.
    
    for i in archsign.read():
        if (counter > DATA_BLOCK_SIZE-1):
	    file.seek(KEYS_SIZE, 1)
	    counter=0
	file.write(i)
	counter+=1
    
    archsign.close()


    # GRABAR LLAVES.
    
    reader.seek(0,0)
    file.seek(0,0)
    countertotal=0
    while(countertotal < 965):
	reader.seek(DATA_BLOCK_SIZE, 1)
    	crudo= reader.read(KEYS_SIZE)
	file.seek(DATA_BLOCK_SIZE, 1)
    	file.write(crudo)
	
        countertotal+=ENTIRE_BLOCK_SIZE
    
    file.close()
    reader.close()


    # GUARDAR FICHERO EN TARJETA.
    os.system("nfc-mfclassic w a processed.mfd >> logs.txt")


    # REMOCION DE ARCHIVOS TEMPORALES.
    os.system("rm huella >> logs.txt")
    os.system("rm processed.mfd >> logs.txt")
    os.system("rm rawcard.mfd >> logs.txt")
    os.system("rm FIRMADO >> logs.txt")
    
    print("USUARIO GRABADO CORRECTAMENTE.")
    
########################################################################    
    
except Exception as e:
    print("REALICE LA OPERACION NUEVAMENTE.")
    exit(1)






















	
