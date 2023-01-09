'''
---------------------------------------------------------------------------------------------------------------------------------------------
												MADE BY G. Estevanus Oscar Toreh
---------------------------------------------------------------------------------------------------------------------------------------------
'''




import sys, os
import hashlib

root = "C:\Ozukaru\Pictures"

daftarH = {}
daftarDuplikat = []




print(" ------------------------------------------ Start Scanning ------------------------------------------ ")
'''
'''
for path, subdirs, files in os.walk(root):
	berkas = sorted(files, key=len)
	for f in berkas:
		h = hashlib.md5(open(path + "\\" + f,'rb').read()).hexdigest()
		print([path, f, h])
		if h not in daftarH:
			daftarH[h] = path + "\\" + f
		else:
			daftarDuplikat.append([path + "\\" + f, daftarH[h]])
			
			
			

print(" ------------------------------------------------------------------------------------------------------- ")
print(" ------------------------------------------ Scanning complete ------------------------------------------ ")
print(" ------------------------------------------------------------------------------------------------------- ")

ada = False
for i in daftarDuplikat:
	print("found duplicate file at " + i[0])
	print("        source : " + i[1])
	ada = True
	
	
print(" ------------------------------------------------------------------------------------------------------- ")

if ada:
	print("do you want to delete duplicated file? y=yes, n=no")
	ask = input(">>")

	if ask == "y":
		for i in daftarDuplikat:
			file = i[0]
			if os.path.exists(file):
				os.remove(file)
			else:
				print("file " + file + " not exist")
		