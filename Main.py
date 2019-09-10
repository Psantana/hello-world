import hashlib
import itertools
def hash_with_sha256(str):
	hash_object = hashlib.sha256(str.encode('utf-8'))
	hex_d = hash_object.hexdigest()
	return hex_d
def main():
	x = input("Enter min password length:")
	y = input("Enter max password length:")
	lis = []
	#Password generated of maximum length J
	for j in range(int(x), int(y)+1):
		for i in itertools.product([0,1,2,3,4,5,6,7,8,9]):
			repeat = int(j)
			lis.append(",".join(map(str,i)))
	print("Password Generated")
	#Opens and reads password_file.txt 
	input_f=open("password_file.txt","r")
	for line in input_f:
		name,salt,hashed_value = line.split(",")
		salt.replace("","")
		hashed_value.replace(" ","")
	print("Applying bruteForce attack for", name)
	for password in lis:
		password.replace("","")
		hex_d=hash_with_sha256(salt+password)
		if(hex_d == hashed_value):
			print(user+"has password"+password)
			break
main()
