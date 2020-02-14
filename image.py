from PIL import Image
	
def rotate_an_image():
	try:    
		path=eval(input("Enter path of image="))
		rt=int(input("Enter degree to rotate="))
		img=Image.open(path)
		img = img.rotate(rt)
		img.save("rotated_picture.jpg") 
		print("check your folder new image 'rotated_picture.jpg' has been saved there")
	except IOError: 
		pass

def transpose_an_image():
	try:    
		path=eval(input("Enter path of image=")) 
		img=Image.open(path)
		img1 = img.transpose(Image.FLIP_LEFT_RIGHT) 	
		img1.save("Fliped_image.jpg") 
		print("check your folder new image with name 'Fliped_image.jpg' has been saved there")
	except IOError: 
		pass		
		

def resize_an_image():
	try:    
		path=eval(input("Enter path of image=")) 
		img=Image.open(path)
		width=int(input('Enter width='))
		height=int(input('Enter height='))
		img1 = img.resize((width, height)) 
		img1.save("resized_image.jpg") 
		print("check your folder new image with name 'resized_image.jpg' has been saved there")
	except IOError: 
		pass		
'''			
def cropping_an_image():
	try:    
		path=eval(input("Enter path of image="))
		img=Image.open(path)
		width=int(input('Enter width='))
		height=int(input('Enter height='))
		area=(0,0,width,height)
		img1=img.crop(area)
        img.save("cropped_image.jpg")
		print("check your folder new image with name 'cropped_image.jpg' has been saved there")
	except IOError:
		pass		
			'''
			
print('MENU')
print('1. rotate an image')
print('2. transpose an image')
print('3. resize an image')
print('4. cropping an image')
print('Enter your option = ');
option=int(input())
if option==1 :
	rotate_an_image()
if option==2 :
	transpose_an_image()
if option==3 :
	resize_an_image()
if option==4 :
	cropping_an_image()

	
