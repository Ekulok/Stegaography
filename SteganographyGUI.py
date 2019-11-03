import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title("Steganography")
root.geometry("500x600")


def Find():
    filename = filedialog.askopenfile()
    print('Selected:', filename)


# def GetPw():
#   var = Pw.get()

# Import File
ImportFrame = tk.LabelFrame(root, text="Import file", padx=10, pady=10)
ImportFrame.place(x=50, y=25, width=150)
Ibutton = ttk.Button(ImportFrame, text="Find...", command=Find).pack(side='top')

# Input Password
PwFrame = tk.LabelFrame(root, text="Password", padx=20, pady=20)
PwFrame.place(x=50, y=100, width=200)

PwSend = tk.StringVar()  # defind as save entry password
EntrySend = tk.StringVar()

Pw = ttk.Entry(PwFrame, show='*')
Pw.pack()


def getPw():
    global PwSend
    PwSend = EntrySend.get()  # read entry password and save it into to PwSend


PwButton = tk.Button(PwFrame, text='Go', command=getPw()).pack(side='right')

# Input textarea
TextFrame = tk.LabelFrame(root, text='Embed Text', padx=10, pady=10)
TextFrame.place(x=50, y=225, height=250, width=400)

TextScroll = tk.Scrollbar(TextFrame)
TextScroll.pack(side='right', fill='y')

TextArea = tk.Text(TextFrame, borderwidth=1, relief='solid')
TextArea.pack(side='left', fill='y')

TextScroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=TextScroll.set)

TextSend = tk.StringVar()
AreaSend = tk.StringVar()

TextArea.pack()


def getText():
    global TextSend
    TextSend = AreaSend.get()


TextButton = tk.Button(root, text='Embed', command=getText())
TextButton.place(x=400, y=475)

root.mainloop()
