from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from run import *
from consts import *


KB = Keyboard()
PB = Plugboard(["AR", "XS", "PO"])
RT_1 = Rotor(rotor_0_1, "K")
RT_2 = Rotor(rotor_0_2, "V")
RT_3 = Rotor(rotor_0_3, "C")
RF = Reflector(reflector_0_1)

# RT_1.rotate_to_letter('H')
# RT_2.rotate_to_letter('M')
# RT_3.rotate_to_letter('C')

input = input("Type your message: ")

output = run_enigma(input.upper(), KB, PB, RT_1, RT_2, RT_3, RF)

print(f"Output: {output}")





