from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import colorchooser



class SteganGUI:
    def __init__(self, master):
        self.root = master
        self.root.config()
        #self.root.geometry("800x800")
        self.root.title("Digital Watermark")

        digitalwatermark(self.root)


class digitalwatermark:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.water_mark = Frame(self.root)
        self.water_mark.grid()

        # Browse file
        def fileDialog():
            try:
                filename = StringVar()
                File = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(
                                                  ("bmp, png files", "*.bmp *.png"),
                                                  ("all file", " *.* ")
                                              ))
                filename.set(File)
                self.file_name = Entry(self.water_mark, textvariable=filename, width=50)
                self.file_name.grid(row=6, column=0, padx=5, pady=5)

                self.original = Image.open(File)
                self.original = self.original.resize((500, 500))  # resize image
                self.img = ImageTk.PhotoImage(self.original)
                self.XY.create_image(0, 0, image=self.img, anchor="nw")  # add係左上
            except:
                print("Please select an image")

        def getlocation(image):
            global x0, y0
            x0 = image.x
            y0 = image.y

        def colorpicker():
            global rgb
            (rgb) = colorchooser.askcolor()

        # OK
        def print_all():
            filename = self.file_name.get()
            embed = self.text_area.get()
            textType = self.clicked_type.get()
            textSize = self.clicked_size.get()
            textBold = self.clicked_bold.get()
            print(filename)
            print(embed)
            print("Type = " + textType)
            print("Size = " + textSize)
            print("Bold = " + textBold)
            print(" X   Y")
            try:
                print(x0, y0)
            except:
                print("Not pick location yet!")
            try:
                print('R, G, B = ' + str(rgb))
            except:
                print("Not pick color yet!")

        # Show address
        self.file_name = Entry(self.water_mark, width=50)
        self.file_name.grid(row=6, column=0, padx=5, pady=5)

        self.browse_button = Button(self.water_mark, text="Browse", command=fileDialog)
        self.browse_button.grid(row=6, column=0, padx=15, pady=15, sticky=W)

        # textarea for watermark
        self.text_label = Label(self.water_mark, text="Watermark text")
        self.text_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.text_area = Entry(self.water_mark, width=30)
        self.text_area.grid(row=1, column=2, padx=20, sticky=N)

        # drop down box (TextType)
        self.type_label = Label(self.water_mark, text="Text Type")
        self.type_label.grid(row=2, column=2, padx=5, pady=5, sticky=NW)
        options_type = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        self.clicked_type = StringVar()
        self.clicked_type.set(options_type[0])
        self.drop_type = OptionMenu(self.water_mark, self.clicked_type, *options_type)
        self.drop_type.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        # drop down box (TextSize)
        self.size_label = Label(self.water_mark, text="Text Size")
        self.size_label.grid(row=3, column=2, padx=5, pady=5, sticky=NW)
        options_size = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        self.clicked_size = StringVar()
        self.clicked_size.set(options_size[0])
        self.drop_size = OptionMenu(self.water_mark, self.clicked_size, *options_size)
        self.drop_size.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        # drop down box (Text Weight)
        self.weight_label = Label(self.water_mark, text="Text Weight")
        self.weight_label.grid(row=4, column=2, padx=5, pady=5, sticky=NW)
        options_bold = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        self.clicked_bold = StringVar()
        self.clicked_bold.set(options_bold[0])
        self.drop_bold = OptionMenu(self.water_mark, self.clicked_bold, *options_bold)
        self.drop_bold.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        # Determin the X, Y by clicking
        # setting up a tkinter window
        self.XY = Canvas(self.water_mark, width=500, height=500, bg='white')
        self.XY.grid(row=0, column=0, rowspan=6, padx=15, pady=15)

        # MouseClick event
        self.XY.bind("<Button 1>", getlocation)

        # ColorPicker
        self.color_button = Button(self.water_mark, text="Pick a Color", command=colorpicker)
        self.color_button.grid(row=5, column=2, padx=5, pady=5, sticky=W)

        # Print all data button
        self.ok_button = Button(self.water_mark, text="OK", command=print_all)
        self.ok_button.grid(row=6, column=2, padx=15, pady=15, sticky=NSEW)

root = Tk()
SteganGUI(root)
root.mainloop()