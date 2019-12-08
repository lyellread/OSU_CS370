# Time Based One Time Password Generator for Google Authenticator
# Lyell Read / 12/7/2019

import qrcode, os, sys, random, time, base64, 

def get_otp():

	print ("get_otp called")

	try:
		keyfile = open("./key", "r")
	except:
		print("Failed to load Key File. Please run " + sys.argv[0] + " --generate-qr \nto generate a QR and corresponding key file.")
		exit()

	key = keyfile.readlines()
	key = otp_key[0].replace("\n", "")

	otp_key = base64.b32decode(key)
	otp_time_step = 30
	otp_time_0 = 0
	otp_time_now = int(time.time())

	otp_time



def generate_qr():

	print ("generate_qr called")

	otp_label = str(input("Label [Example] :") or "Example")
	otp_user = str(input("User [alice@google.com] :") or "alice@google.com")

	keyfile = open("./key", "w")
	otp_key = ''.join([random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for u in range (0,16)])
	keyfile.write(otp_key)
	keyfile.close()

	#otpauth://totp/Example:alice@google.com?secret=Q4O9E5POMAQZSIG8&issuer=Example
	#otpauth://totp/Example:alice@google.com?secret=Q4O9E5POMAQZSIG8&issuer=Example
	
	#otp_key='JBSDD3DPEHPK3PXP'
	ga_uri = "otpauth://totp/" + otp_label + ":" + otp_user + "?secret=" + otp_key + "&issuer=" + otp_label

	print(ga_uri)

	qrcode.make(ga_uri).save("./qr_code.png")

	print("Success: OTP QR Code created and saved as ./qr_code.png")

	return


if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()
	if sys.argv[1] == "--generate-qr":
		generate_qr()
		exit()
	elif sys.argv[1] == "--get-otp":
		get_otp()
		exit()
	else:
		print("Improper Argument(s) Provided. Quitting.")
		exit()
