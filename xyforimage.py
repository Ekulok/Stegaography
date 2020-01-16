from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog

root = Tk()

#setting up a tkinter window
w = Canvas(root, width=500, height=500)
w.pack()

#adding the image
File = askopenfilename(parent=root, initialdir="./",title='Select an image')
original = Image.open(File)
original = original.resize((500,500)) #resize image
img = ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw") #add係左上

# Determine the X, Y by clicking
def getlocation(image):
    global x0, y0
    x0 = image.x
    y0 = image.y
    print('X, Y from 左上')
    print(x0, y0)
#mouseclick event
w.bind("<Button 1>",getlocation)

root.mainloop()