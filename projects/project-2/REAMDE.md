## TOTP Generator README

NOTES: 
 - Could not test on Android, works on iOS.
 - This is meant to run with Python 3.*. 
 - You must run `--generate-qr` before `--get-otp`.

This program is run as follows:

```
$ python3.7 totp --generate-qr
```

...will interactively generate a URI and turn it into a QR Code in the current directory. It will also generate a key in the local directory used in the next step. 

```
$ python3.7 totp --get-otp
```

...will print out the same OTP as the Google Authenticator app by performing the following steps (high level, see program for more details):

1. Find the offset from time 0
2. Compute the SHA-1 HMAC from that value
3. Find the 4 bytes used in the calculation of the OTP
4. Turn those 4 bytes into the OTP