from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

## GUARDAR CLAVE PRIVADA
from cryptography.hazmat.primitives import serialization
pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.TraditionalOpenSSL,
   encryption_algorithm=serialization.NoEncryption()
)
pem.splitlines()[0]

file = open("privateKey", "wt")
file.write(pem)
file.close

## GUARDAR CLAVE PUBLICA.
public_key = private_key.public_key()
pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
pem.splitlines()[0]

file = open("publicKey", "wt")
file.write(pem)
file.close
