import sys
import os

sys.path.append(f'{os.getcwd().split("user_interface")[0]}\\functions')
sys.path.append(os.getcwd())

import barcode_functions
import settings_functions

from tkinter import *
import PIL.Image

class Displays:
    def __init__(self, root):
        self.root = root
        self.root.configure(background='#1A1A1A')

        self.canvas = Canvas(highlightthickness=0)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.load_photos()

    def display_main_activity(self):
        self.canvas.delete('all')

        self.canvas.create_image(0, 0, image=self.ma_background, anchor = NW)

        self.canvas.create_image(225, 400, image=self.ma_input, anchor=NW)

        code_input = Entry(justify=CENTER)
        code_input.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Roboto', 28))
        code_input.focus()
        code_input.bind("<Return>", (lambda event: barcode_functions.generate_barcode(code_input.get())))

        self.canvas.create_window(226, 401, window=code_input, anchor=NW, width=148, height=48)

        settings_button = Button(self.root, image=self.ma_settings_button, bd=0, bg='#1A1A1A', activebackground='#1A1A1A', command = self.display_settings_activity)

        self.canvas.create_window(0, 950, window=settings_button, anchor=NW)

    def display_settings_activity(self):
        self.root.update()
        self.canvas.delete('all')

        settings_data = list(settings_functions.read_settings().values())
        print(settings_data)

        self.canvas.create_image(0, 0, image=self.sa_background, anchor = NW)

        exit_button = Button(self.root, image=self.sa_exit_button, bd=0, bg='#1A1A1A', activebackground='#1A1A1A', command = self.display_main_activity)

        self.canvas.create_window(0, 0, window=exit_button, anchor=NW)

        height_input = Entry(justify=CENTER)
        height_input.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Lora', 30))
        height_input.insert(0, settings_data[0])
        self.canvas.create_window(350, 250, window=height_input, anchor = NW, width = 75, height = 38)

        width_input = Entry(justify=CENTER)
        width_input.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Lora', 30))
        width_input.insert(0, settings_data[1])
        self.canvas.create_window(350, 300, window=width_input, anchor = NW, width = 75, height = 38)

        font_size = Entry(justify=CENTER)
        font_size.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Lora', 30))
        font_size.insert(0, settings_data[2])
        self.canvas.create_window(350, 350, window=font_size, anchor = NW, width = 75, height = 38)

        text_distance = Entry(justify=CENTER)
        text_distance.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Lora', 30))
        text_distance.insert(0, settings_data[3])
        self.canvas.create_window(350, 400, window=text_distance, anchor = NW, width = 75, height = 38)

        quiet_zone = Entry(justify=CENTER)
        quiet_zone.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Lora', 30))
        quiet_zone.insert(0, settings_data[4])
        self.canvas.create_window(350, 450, window=quiet_zone, anchor = NW, width = 75, height = 38)

        checksum = Entry(justify=CENTER)
        checksum.config(bg='#1A1A1A', bd = 0, fg='#FF3B30', font=('Lora', 30))
        checksum.insert(0, settings_data[5])
        self.canvas.create_window(350, 500, window=checksum, anchor = NW, width = 75, height = 38)

        save_button = Button(self.root, image=self.sa_save_button, bd=0, bg='#1A1A1A', activebackground='#1A1A1A', command = lambda : settings_functions.write_data({'module_height' : height_input.get(), 'module_width' : width_input.get(), 'font_size' : font_size.get(), 'text_distance' : text_distance.get(), 'quiet_zone' : quiet_zone.get(), 'checksum' : checksum.get()}))
        self.canvas.create_window(225, 575, window = save_button, anchor = NW, width = 150, height = 50)

        preview_button = Button(self.root, image=self.sa_preview_button, bd=0, bg='#1A1A1A', activebackground='#1A1A1A', command = self.display_preview_activity)
        self.canvas.create_window(225, 675, window = preview_button, anchor = NW)

    def display_preview_activity(self):
        barcode_functions.generate_barcode('test1234')

        img_path = f"{os.getcwd().split('user_interface')[0]}\\images\\temp\\"
        img_size = PIL.Image.open(f'{img_path}barcode.png')

        window = Toplevel(self.root)
        window.geometry(f'{img_size.width}x{img_size.height}')

        img_photo = PhotoImage(file=f'{img_path}barcode.png')
        img = Label(window, image=img_photo)
        img.place(x=0, y=0)

        window.mainloop()


    def load_photos(self): # threading, display_loading_activity
        ma_dir = f"{os.getcwd().split('user_interface')[0]}\\images\\display_main_activity\\"
        sa_dir = f"{os.getcwd().split('user_interface')[0]}\\images\\display_settings_activity\\"

        self.ma_background = PhotoImage(file=f'{ma_dir}background.png')
        self.ma_settings_button = PhotoImage(file=f'{ma_dir}settings_button.png')
        self.ma_input = PhotoImage(file=f'{ma_dir}input.png')

        self.sa_background = PhotoImage(file = f'{sa_dir}background.png')
        self.sa_exit_button = PhotoImage(file = f'{sa_dir}exit_button.png')
        self.sa_save_button = PhotoImage(file = f'{sa_dir}save_button.png')
        self.sa_preview_button = PhotoImage(file = f'{sa_dir}preview_button.png')

