import os, PIL.Image
from tkinter import *

def display_preview_activity():
    img_path = f"{os.getcwd().split('user_interface')[0]}\\images\\temp\\"
    img_size = PIL.Image.open(f'{img_path}barcode.png')

    root = Tk()
    root.geometry(f'{img_size.width}x{img_size.height}')

    img_photo = PhotoImage(file=f'{img_path}barcode.png')
    img = Label(root, image=img_photo)
    img.place(x=0, y=0)
    root.mainloop()

display_preview_activity()
