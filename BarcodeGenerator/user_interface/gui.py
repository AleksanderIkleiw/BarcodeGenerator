import sys, os
from tkinter import *
from user_interface import displays
class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x1000')
        self.root.resizable(False, False)
        self.root.wm_attributes('-toolwindow', False)

        self.displays = displays.Displays(self.root)

    def main(self):
        self.displays.display_main_activity()

        self.root.mainloop()


if __name__ == '__main__':
    obj = GUI()
    obj.main()
