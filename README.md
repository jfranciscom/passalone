# passalone
Small but very complex Python project including cryptography, rfid, keycards, fingerprint scanners, Raspberry Pi and desktop interface.

This project consists in an offline physical autentication system, where an administrator with a tkinter program creates keycards containing the user's 'hashed' fingerprint, which later will be used for allowing the user to enter any facility.

The user must present his keycard to the entrance of the facility he wants later to enter, where a Raspberry Pi containing a fingerprint scanner, battery and RFID module will check if he is allowed. To be authenticated, the user has to place his finger on the scanner and the keycard in the RFID module at the same time and match both.

In comparison with other fingerprint authentication systems, here, we allow the administrators to carry the authenticator system anywhere, without the need of a database or any communication, making it standalone. The system, with a battery, could run from the deepest caves to, possibly, the Moon.
