# Time Based One Time Password Generator for Google Authenticator
# Lyell Read / 12/7/2019
# Citations: 
# - https://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python
# - https://tools.ietf.org/html/rfc4226
# - https://tools.ietf.org/html/rfc6238

import qrcode, os, sys, random, time, base64, struct, hashlib, hmac

def get_otp():

	try:
		keyfile = open("./key", "r")
	except:
		print("Failed to load Key File. Please run " + sys.argv[0] + " --generate-qr \nto generate a QR and corresponding key file.")
		exit()

	key = keyfile.readlines()
	key = key[0].replace("\n", "")

	otp_key = base64.b32decode(key)
	otp_time_step = 30
	otp_time_0 = 0
	otp_time_now = int(time.time())

	# generate the iterations to the current unix time. Note '//' instead 
	# of '/' as this will discard the remainder and essentially 'round down' 
	# or floor as describved in https://tools.ietf.org/html/rfc6238#section-4.2
	otp_intervals = (otp_time_now - otp_time_0)//30

	# generate struct of bytes from the intervals to be passed to the hash function
	# as a big endian unsigned long long
	otp_intervals = struct.pack(">Q", otp_intervals)

	# run HMAC SHA 1 as in https://tools.ietf.org/html/rfc4226#section-5.2 wiht
	# the otp_intervals as the 'message' and otp_key as the key
	otp_hash_out = hmac.new(otp_key, otp_intervals, hashlib.sha1).hexdigest()

	# https://tools.ietf.org/html/rfc4226#section-5.4
	otp_start_index = int(otp_hash_out[-1:], 16)	
	
	# get bytes at proper index, per https://tools.ietf.org/html/rfc4226#section-5.4
	otp_hash_subset = otp_hash_out[otp_start_index*2 : (otp_start_index*2)+8]
	
	# convert those bytes to int (using int(hex, 16) --> int) and and them with 0x7fffffff
	# as described inhttps://tools.ietf.org/html/rfc4226#section-5.4
	otp_code = (int("0x" + str(otp_hash_subset), 16) & 0x7fffffff) % 1000000

	print(otp_code)

	return



def generate_qr():

	#print ("generate_qr called")

	otp_label = str(input("Label [Example] :") or "Example")
	otp_user = str(input("User [alice@google.com] :") or "alice@google.com")

	keyfile = open("./key", "w")
	otp_key = ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for u in range (0,16)])
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
