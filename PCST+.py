import tkinter as tk
from tkinter.ttk import Combobox
import subprocess
from tkinterdnd2 import *
import pyperclip

class pcst(TkinterDnD.Tk):

    def __init__(self):
        TkinterDnD.Tk.__init__(self)
        self.window_height = 250
        self.window_width = 250

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coords = int((screen_width / 2) - (self.window_width / 2))
        y_coords = int((screen_height / 2) - (self.window_height / 2))

        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_coords, y_coords))
        self.minsize(width=250, height=250)
        self.maxsize(width=250, height=250)

        self.lbl = tk.Label(self, text="Welcome to PCST+", font=("Consolas Bold", 20))
        self.lbl.pack()
        self.btn = tk.Button(self, text="Get checksum", font=("Corbel Bold", 20), command=self.getchecksum)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="Verify checksum", font=("Corbel Bold", 20), command=self.verifychecksum)
        self.btn2.pack()
        self.lblinfo = tk.Label(self, text="First build, don't mind that GUI is ugly.", font=("Consolas Bold", 8))
        self.lblinfo.pack()

        self.lbl2 = tk.Label(self, text="Select hash type:", font=("Consolas", 15))
        self.combo = Combobox(self, width=39) 
        self.combo['values'] = ("SHA1", "SHA256", "SHA384", "SHA384", "SHA512", "MD2", "MD4", "MD5")  
        self.combo.current(0)
        self.lbl3 = tk.Label(self, text="Enter file's path:", font=("Consolas", 15))
        self.entry_sv = tk.StringVar()
        self.entry = tk.Entry(self, textvar=self.entry_sv, width=40)
        self.begin = tk.Button(self, text="Start", command=self.start, font=("Corbel Bold", 15))
        self.begin2 = tk.Button(self, text="Start", command=self.start2, font=("Corbel Bold", 15))
        self.entry.drop_target_register(DND_FILES)
        self.entry.dnd_bind('<<Drop>>', self.drop)
    
    def verifychecksum(self):
        self.lbl.destroy()
        self.btn.destroy()
        self.btn2.destroy()
        self.lbl2.pack()
        self.combo.pack()
        self.lbl3.pack()
        self.entry.pack()
        self.lbl5 = tk.Label(self, text="Enter the checksum", font=("Consolas", 15))
        self.lbl5.pack()
        self.entry2 = tk.Entry(self, width=40)
        self.entry2.pack()
        self.begin2.pack()

    def drop(self, event):
        self.entry_sv.set(event.data)

    def getchecksum(self):
        self.lbl.destroy()
        self.btn.destroy()
        self.btn2.destroy()
        self.lbl2.pack()
        self.combo.pack()
        self.lbl3.pack()
        self.entry.pack()
        self.begin.pack()
    
    def gets(self):
        self.entri = self.entry.get()
        self.comboget = self.combo.get()
    
    def gets2(self):
        self.entri2 = self.entry2.get()
    
    def copy(self):
        pyperclip.copy(f"{self.newoutput[1]}")
        self.btn3.configure(text="Copied")

    def quit(self):
        app.destroy()
    
    def start(self):
        self.gets()
        self.output = subprocess.run(["certutil", "-hashfile", self.entri, self.comboget], stdout=subprocess.PIPE, text=True)
        self.newoutput = self.output.stdout.split("\n")
        self.lbl4 = tk.Label(self, text = f"{self.newoutput[1]}")
        self.lbl4.pack()
        self.btn3 = tk.Button(self, text="Copy checksum", command = self.copy, font=("Corbel Bold", 15))
        self.btn3.pack()
        self.btn4 = tk.Button(self, text="Quit PCSV", command=self.quit, font=("Corbel Bold", 15))
        self.btn4.pack()

    def start2(self):
        self.gets()
        self.gets2()
        self.output = subprocess.run(["certutil", "-hashfile", self.entri, self.comboget], stdout=subprocess.PIPE, text=True)
        self.newoutput = self.output.stdout.split("\n")
        if self.entri2 == self.newoutput[1]:
            self.begin2.configure(text=f"The checksums matches!")
        if self.entri2 != self.newoutput[1]:
            self.begin2.configure(text="The checksums doesn't match.")
        self.btnquit = tk.Button(self, text="Quit PCSV", command=self.quit, font=("Corbel Bold", 15))
        self.btnquit.pack()
app = pcst()
app.mainloop()