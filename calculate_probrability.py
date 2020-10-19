#图形
# from PIL import Image
# img=Image.open("getcwd()+"img_res\\bblack.png")
# img.show()
# img.save("temp.png")




# img.getpixel((100,100))
# img.convert("L").getpixel((100,100))
count=0
from math import acos
for i in range(60):
	for j in range(60):
		if abs(i-j)<=15:
			count+=1
print ("%d/%d"%(count/225,60*60/225))