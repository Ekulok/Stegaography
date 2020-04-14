
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyqrcode
import os



class SteganGUI:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.geometry("800x600")
        self.root.title("QR Code Generator")

        qrcode(self.root)


class qrcode:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.qrcode = Frame(self.root)
        self.qrcode.grid()

        def generate():
            if len(subject.get()) != 0:
                global myQr
                myQr = pyqrcode.create(subject.get())
                qrImage = myQr.xbm(scale=6)
                global photo
                photo = BitmapImage(data=qrImage)
            else:
                messagebox.showinfo("Error!", "Please Enter The Subject")
            try:
                showCode()
            except:
                pass

        # code showing
        def showCode():
            global photo
            self.notificationLabel.config(image=photo)
            self.subLabel.config(text="Showing QR Code for: " + subject.get())

        def save():
            # folder to save all the codes
            dir = path1 = os.getcwd() + "\\QR Codes"

            # create a folder is it doesn't exist
            if not os.path.exists(dir):
                os.makedirs(dir)

            try:
                if len(name.get()) != 0:
                    qrImage = myQr.png(os.path.join(name.get() + ".png"), scale=6)
                else:
                    messagebox.showinfo("Error!", "File name can not be empty!")
            except:
                messagebox.showinfo("Error!", "Please generate the code first")

        def fileDialog():
            filename.set(filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(
                                                        ("bmp, wav, png, flac files", "*.bmp *.wav *.png *.flac"),
                                                        ("all files", " *.* "))))

        self.top_title = Label(self.qrcode, text="QR code")
        self.top_title.grid(row=1, column=1)

        self.lab1 = Label(self.qrcode, text="Enter Subject:")
        self.lab1.grid(row=2)

        self.lab2 = Label(self.qrcode, text="Enter File Name:")
        self.lab2.grid(row=3)

        subject = StringVar()
        self.subjectEntry = Entry(self.qrcode, textvariable=subject)
        self.subjectEntry.grid(row=2, column=1, sticky=E + W)

        name = StringVar()
        self.nameEntry = Entry(self.qrcode, textvariable=name)
        self.nameEntry.grid(row=3, column=1, sticky=E + W)

        self.createButton = Button(self.qrcode, text="Create QR Code", command=generate)
        self.createButton.grid(row=2, column=2)

        #QR code
        self.notificationLabel = Label(self.qrcode)
        self.notificationLabel.grid(row=5, column=1)

        #show QR code name
        self.subLabel = Label(self.qrcode, text="")
        self.subLabel.grid(row=6, column=1)

        self.showButton = Button(self.qrcode, text="Save as PNG", command=save)
        self.showButton.grid(row=3, column=2)


        self.file_browse = Label(self.qrcode, text="File: ")
        self.file_browse.grid(row=4)

        filename = StringVar()
        self.file_name = Entry(self.qrcode, textvariable=filename, width=40)
        self.file_name.grid(row=4, column=1)

        self.browse_button = Button(self.qrcode, text="Browse", command=fileDialog)
        self.browse_button.grid(row=4, column=2)

root = Tk()
SteganGUI(root)
root.mainloop()