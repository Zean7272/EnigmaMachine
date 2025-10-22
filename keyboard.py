from consts import *
class Keyboard:

    def forward(self, letter):
        # if letter == " ":
        #     letter = "z"
        # if letter == ",":
        #     letter = "%"
        # if letter == ".":
        #     letter = "*"

        signal = alpha_0.find(letter)
        print(f"keyboard forward: {letter}")
        return signal

    def backward(self, signal):
        letter = alpha_0[signal]
        # if letter == "z":
        #     letter = " "
        # if letter == "%":
        #     letter = ","
        # if letter == "*":
        #     letter = "."
        print(f"keyboard backward: {letter}")
        return letter

# kb = Keyboard()
# print(kb.forward("C"))
# print(kb.backward(2))
