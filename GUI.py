from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from run import *
from consts import *
import customtkinter as ctk


KB = Keyboard()
PB = Plugboard(["AR", "XS", "PO"])
RT_1 = Rotor(rotor_0_1, "K")
RT_2 = Rotor(rotor_0_2, "V")
RT_3 = Rotor(rotor_0_3, "C")
RF = Reflector(reflector_0_1)

RT_1.rotate_to_letter('H')
RT_2.rotate_to_letter('M')
RT_3.rotate_to_letter('C')


class GUI:

    def __init__(self, master):
        self.master = master

        self.main_frame = ctk.CTkFrame(self.master)
        self.main_frame.pack(expand=True, fill='both')

        self.set_frame = ctk.CTkFrame(self.main_frame)
        self.set_frame.pack(side='left', fill='both', expand=True)

        self.set_lb = ctk.CTkLabel(self.set_frame, text="Settings", font=('Calibri', 30))
        self.set_lb.pack(pady=10, padx=10)

        self.btn = ctk.CTkButton(self.set_frame, font=('Calibri', 30), text='Cipher', command=lambda: self.encipher())
        self.btn.pack(side='bottom')

        self.in_frame = ctk.CTkFrame(self.main_frame)
        self.in_frame.pack(side='left', fill='both', expand=True)

        self.in_lb = ctk.CTkLabel(self.in_frame, text="Input", font=('Calibri', 30))
        self.in_lb.pack(pady=10, padx=10)

        self.in_box = ctk.CTkTextbox(self.in_frame, font=('Calibri', 30), wrap='word')
        self.in_box.pack(pady=10, padx=10, expand=True, fill='both')

        self.out_frame = ctk.CTkFrame(self.main_frame)
        self.out_frame.pack(side='left', fill='both', expand=True)

        self.out_lb = ctk.CTkLabel(self.out_frame, text="Output", font=('Calibri', 30))
        self.out_lb.pack(pady=10)

        self.out_box = ctk.CTkTextbox(self.out_frame, font=('Calibri', 30), wrap='word')
        self.out_box.configure(state='disabled')
        self.out_box.pack(pady=10, padx=10, expand=True, fill='both')

    def read_input(self):
        input = self.in_box.get('0.0', 'end-1c').upper()
        return input

    def encipher(self):
        output = run_enigma(self.read_input(), KB, PB, RT_1, RT_2, RT_3, RF)
        self.show_output(output)

    def show_output(self, output):
        self.out_box.configure(state='normal')
        self.out_box.insert('end', "{}".format(output).lower())
        self.out_box.configure(state='disabled')

