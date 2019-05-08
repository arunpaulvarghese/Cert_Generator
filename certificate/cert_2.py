# import required classes

from PIL import Image, ImageDraw, ImageFont
import img2pdf
import os
import PIL
import csv
from fpdf import FPDF
newshit=[]
# create Image object with the input image

with open('names.csv','rb') as f:
	reader=csv.reader(f)
	your_list=list(reader)

'''
for i in range(len(your_list)):
	print "Entry "+str(i+1)+" "+your_list[i][0]+your_list[i][1]
'''
#print your_list[1][0]
#writer = csv.writer(open('emails.csv', 'w'))
filename=""
for i in range(len(your_list)):
	image = Image.open('certificate.jpg').convert('RGB')

	# initialise the drawing context with
	# the image object as background

	draw = ImageDraw.Draw(image)
	# desired size
		 
	font = ImageFont.truetype('Nexa Bold.otf', size=80)
		 
	# starting position of the message
	#message = str(your_list[i][0]+" "+your_list[i][1])
	message=your_list[i][0]
	filename=message
	if len(message)>=18:
		(x, y) = (1450, 1000)
	else:
		(x, y) = (1450, 1000)
		
	#message=message[2:len(message)-2]
	color = 'rgb(0, 0, 0)' # black color
		 
	# draw the message on the background
		 
	draw.text((x, y), message, fill=color, font=font)
	'''

	message="800"
	font = ImageFont.truetype('Nexa Bold.otf', size=100)
	draw.text((750,1375), message, fill=color, font=font)
	'''
	'''
	(x, y) = (120, 900)
	place = 'Kalady, Kerala, India'
	color = 'rgb(0, 0, 0)' # white color
	draw.text((x, y), place, fill=color, font=font)
		 
	#Add date

	(x, y) = (205, 1080)
	date = 'Dec 4th 2018'
	color = 'rgb(0, 0, 0)' # white color
	draw.text((x, y), date, fill=color, font=font)
	'''

	# save the edited image
	#filename=str(your_list[i][0])+str(your_list[i][1])
	#filename=filename[2:len(filename)-2]
	fileloc='pdfs/'+filename+'.png'
	#image.save(fileloc)
	pdf_name=fileloc[0:len(fileloc)-4]+'.pdf'
	#print pdf_name
	'''
	newshit.append([[your_list[i][0]],[your_list[i][1]],[your_list[i][2]],[pdf_name]])
	print i
	print newshit[i][0][0]+","+newshit[i][1][0]+","+newshit[i][2][0]+","+newshit[i][3][0]
	'''
	image.save(pdf_name,"PDF",resolution=100.0)
	#print pdf_name
	print "Saved "+str(i)
'''
with open("emails.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in range(len(newshit)):
		wr.writerow([newshit[i][0][0],newshit[i][1][0],newshit[i][2][0],newshit[i][3][0]])
'''