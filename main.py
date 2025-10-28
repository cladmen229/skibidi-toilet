from customtkinter import *
from PIL import Image, ImageFilter, ImageEnhance

win = CTk()
win.geometry('550x600')

image = Image.open('1023.avif')
image_ctk = CTkImage(light_image= image, size = (500, 400))
lbl_image = CTkLabel(win, text = '', image= image_ctk)
lbl_image.pack(pady = 50)

frame = CTkFrame(win)
frame.pack(side= 'bottom', pady = (0,25))

angle = 0
def rotate_image():
    global angle, image
    if angle <= 360:
        angle += 90
        image_ctk.configure(light_image = image.rotate(angle))
    else:
         angle = 0
    lbl_image.configure(image = image_ctk)

def  do_bw():
    global image
    image = image.convert('L')
    image_ctk.configure(light_image = image.rotate(angle))
    lbl_image.configure(image = image_ctk)

def  do_blur():
    global image
    image = image.filter(ImageFilter.BLUR)
    image_ctk.configure(light_image = image.rotate(angle))
    lbl_image.configure(image = image_ctk)

def do_contrast(value):
    global image
    enhacer = ImageEnhance.Contrast(image)
    image = enhacer.enhance(value/50)
    image_ctk.configure(light_image = image)
    lbl_image.configure(image = image_ctk)



btn_rotate = CTkButton(frame, text = 'Rotate 90', command=rotate_image)
btn_rotate.grid(row = 0, column = 0, padx= 10)

btn_rotate = CTkButton(frame, text = 'Black & White', command=do_bw)
btn_rotate.grid(row = 0, column = 1)

btn_rotate = CTkButton(frame, text = 'Blur', command=do_blur)
btn_rotate.grid(row = 0, column = 2, padx= 10)

lbl_contrast = CTkLabel(frame, text = 'Contrast')
lbl_contrast.grid(row = 1, column = 1)

slider = CTkSlider(frame, from_= 0, to= 100, command= do_contrast)
slider.grid(row = 2, column = 1)

win.mainloop()