import binascii

BASE_256="output-f-0-sha256"
BASE_512="output-f-0-sha512"


def diff(a, b):

	a = bin(int(binascii.hexlify(a), 16))[2:] 
	b = bin(int(binascii.hexlify(b), 16))[2:] 

	counter = 0

	for x in range (0, len(a)):
		if a[x] != b[x]:
			counter += 1

	return counter


def bindiff_files(base, output):

	B = open(base,'r')
	b_data = B.readlines()[0][len(base) + 6:-2]
	B.close()

	O = open(output,'r')
	o_data = O.readlines()[0][len(output) + 6:-2]
	O.close()

	_diff = diff(b_data, o_data)
	print ("DIFF " + str(base) + ", " + str(output) + ": " + str(_diff))


diffs =[1, 49, 73, 113]
for bit_diff in diffs:

	bindiff_files(BASE_256, "output-f-" + str(bit_diff) + "-sha256")
	bindiff_files(BASE_512, "output-f-" + str(bit_diff) + "-sha512")

