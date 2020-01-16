from tkinter import colorchooser
from tkinter import *

root = Tk()

# rgb
(rgb, hx) = colorchooser.askcolor()
print('R, G, B = ' + str(rgb) + ' hex = ' + hx)

root.mainloop()