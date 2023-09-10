import tkinter as tk
import tkinter.messagebox

'''
Window class for installer application
'''
class Installer(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("SimpleMark Installer")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.page()

    def on_exit(self):
        if tk.messagebox.askyesno("SimpleMark Installer", "Are you sure you want to quit?"):
            self.destroy()

    '''
    Runs the main installer page
    '''
    def page(self):
        frame = tk.Frame()
        frame.pack()

        greeting = tk.Label(master=frame, text="SimpleMark Installer")
        greeting.pack()


Installer().mainloop()
