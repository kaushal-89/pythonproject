from PIL import Image
import os
import io
from array import array

#CONVERT JPG TO TIFF
image = Image.open('AOFOrginal.jpg')
#image.show()
image.save('AOFJpgToTiff.tiff')
#image.show()
print("testing")
#CONVERT TIFF TO BYTES

def readimage(path):
	with open(path, "rb") as f:
			  return bytearray(f.read())
			  
#CONVERT BYTES BACK TO TIFF
		
bytes = readimage('AOFJpgToTiff.tiff')

#file1 = open("aofbytes.txt","w")
#file1.write("test ing")
print(bytes[:50])
image = Image.open(io.BytesIO(bytes))
image.save('AOFByteToTiff.tiff')
#image.show()