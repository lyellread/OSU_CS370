# Time Based One Time Password Generator for Google Authenticator
# Lyell Read / 12/7/2019

import qrcode
import os
import sys

def generate_qr():

	print ("generate_qr called")


def get_otp():

	print ("get_otp called")





if __name__ == "__main__":
	
	if sys.argv[1] == "--generate-qr":
		generate_qr()
		exit()
	elif sys.argv[2] == "--get-otp":
		get_otp()
		exit()
	else:
		print("Improper Argument(s) Provided. Quitting.")
		exit()
