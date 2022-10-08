#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import binascii
import time
import base64
from struct import *
from pyfingerprint.pyfingerprint import PyFingerprint
import os
import cryptography.exceptions
from datetime import datetime as dt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key



def autenticar():
	KEYS_SIZE		= 16
	ENTIRE_BLOCK_SIZE	= 64
	DATA_BLOCK_SIZE		= 48
	CHARACT_REAL_SIZE	= 512
	CHARACT_COMPRESSED_SIZE	= 256
	POS_CHARACTS		= 320
	POS_SIGN		= 672
	POS_SEPARATOR		= 656

	valid_thru_ok		= 0
	biometrics_ok		= 0
	signature_ok		= 0


	try:
	    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

	    if ( f.verifyPassword() == False ):
		raise ValueError('The given fingerprint sensor password is wrong!')

	except Exception as e:
	    print('FALLA EN EL LECTOR.')
	    exit(1)
	##########################################################################################################################
	try:
	    os.system("nfc-mfclassic r a userCard.mfd >> logs.txt")
	    file = open("userCard.mfd","rb")
	    crudo = ""
	    file.seek(ENTIRE_BLOCK_SIZE, 0)
	    for i in range(1, 1008):
		crudo += file.read(48)
		file.seek(KEYS_SIZE, 1)

	    print "APOYE SU HUELLA SOBRE EL LECTOR."
	    # LEER HUELLA DEL CLIENTE.
	    while (f.readImage() == False):
		pass
	    
	    print
		# Guardo huella en posiciOn 1.
	    f.convertImage(0x01)
	    arch = open("HUELLADEDOCOMP.txt", "wt")
	    characts1 = f.downloadCharacteristics(0x01)
	    arch.write(str(characts1))
	    arch.close()
	    #print(len(characts1))

	    # PROCESAR DATOS DE USUARIO.
	    
	    userdata = crudo.split('[')[1].split(']')[0].split(';')
	    validthru = crudo.split('[')[2].split(']')[0]
	    
	    # VERIFICAR FECHA DE CADUCIDAD.

	    fechacaduc = dt.strptime(validthru, "%d/%m/%Y")
	    
	    if (fechacaduc > dt.today()):
		print ("Credencial vigente.")
		valid_thru_ok = 1
	    else:
		print ("Credencial CADUCADA.")
		valid_thru_ok = 0
	    


	    # LEER BIOMETRIA DE LA TARJETA.
	    # Posicion inicial POS_CHARACTS = h140.
	    file.seek(POS_CHARACTS, 0)
	    huella = []
	    
	    ct = 0 # Cuenta para no pisar las llaves.
	    for i in file.read(CHARACT_COMPRESSED_SIZE+80):
		if(not ct in range(48, ENTIRE_BLOCK_SIZE) and not ct in range(112, 128) and not ct in range(176, 192) and not ct in range(240, CHARACT_COMPRESSED_SIZE) and not ct in range(304, POS_CHARACTS) and not ct in range(368, 384)):
		    #print ("NO: " + i)
		    huella.append(i)
		#else:
		    #print ("SI: " + i)
		    
		# Agrego ceros que faltan.
		ct += 1
	    for i in range(0, (CHARACT_REAL_SIZE-CHARACT_COMPRESSED_SIZE)):
		huella.append(chr(0))

	    
		# Convierto hex a int.
	    characts2 = []
	    for i in huella:
		characts2.append(int(str(format(ord(i),"x")), KEYS_SIZE))
	   
	    # COMPROBAR HUELLA.
		# Fichero temporal sobre la huella que se obtuvo de la tarjeta.
	    arch = open("HUELLALEIDA.txt", "wt")
	    arch.write(str(characts2))
	    arch.close()
	    f.uploadCharacteristics(0x02, characts2)
	    if ( f.compareCharacteristics() != 0 ):
		
		print("Biometria confirmada.")
		biometrics_ok = 1
	    else:
		print("Datos biometricos incorrectos.")
		biometrics_ok = 0
	    
	    # LEER FIRMA DE LA TARJETA.
	    # Posicion inicial 2a0 = POS_SIGN.
	    ct = 0
	    firma = []
	    file.seek(POS_SIGN,0)
		# Leo la firma.
	    for i in file.read(336):
		if(not ct in range(KEYS_SIZE, 32) and not ct in range(80, 96) and not ct in range(144, 160) and not ct in range(208, 224) and not ct in range(272, 288)):
		    firma.append(i)
		ct += 1
	    file.close()

		# Guardo firma en archivo.
	    file = open("signature.sig", "wb")
	    for i in firma:
		file.write(i)
	    file.close()


	    # PROCESAR FIRMA
	       #Aplico plantilla.
	    sinPicar = "["
	    for i in userdata:
		sinPicar += i + ";"

	    sinPicar = sinPicar[:-1] + "][" + str(validthru) + "]" + str(characts2)
		#Hasheo.
	    picadillo = hashlib.sha224(sinPicar).hexdigest()
	    
	    # Load the public key.
	    with open('publicKey', 'rb') as f:
		public_key = load_pem_public_key(f.read(), default_backend())
	    
	    # Load the payload contents and the signature.

	    with open('signature.sig', 'rb') as f:
		signature = f.read()

	    # Perform the verification.
	    try:
		public_key.verify(
		    signature,
		    picadillo,
		    padding.PSS(
		        mgf = padding.MGF1(hashes.SHA256()),    
		        salt_length = padding.PSS.MAX_LENGTH,
		    ),
		    hashes.SHA256(),
		)
		print ("Firma validada.")
		signature_ok = 1
	    except cryptography.exceptions.InvalidSignature as e:
		print("Firma invalida.")
		signature_ok = 0

	    
	    ## PRUEBA FINAL.

	    if(biometrics_ok == 1 and signature_ok == 1 and valid_thru_ok == 1):
		print ("USUARIO AUTENTICADO.")
	    else:
		print ("FALLO EN LA AUTENTICACION.")
		if (biometrics_ok == 0):
		    print ("La huella ingresada no coincide.")
		if (signature_ok == 0):
		    print ("Datos de tarjeta corrompidos.")
		if (valid_thru_ok == 0):
		    print ("Tarjeta caducada.")

	    # REMOCION DE ARCHIVOS TEMPORALES.
	    os.system("rm HUELLALEIDA.txt")
	    os.system("rm HUELLADEDOCOMP.txt")
	    os.system("rm userCard.mfd")
	    os.system("rm signature.sig")
	########################################################################    
	 
	except Exception as e:
	    print("FALLO EN LA AUTENTICACION.")
	    exit(1)






















	
