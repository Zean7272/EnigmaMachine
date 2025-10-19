from consts import *
class Keyboard:

    def forward(self, letter):
        if letter == " ":
            letter = "z"
        if letter == ",":
            letter = "%"
        if letter == ".":
            letter = "*"

        signal = alpha_0.find(letter)
        return signal

    def backward(self, signal):
        letter = alpha_0[signal]
        if letter == "z":
            letter = " "
        if letter == "%":
            letter = ","
        if letter == "*":
            letter = "."
        return letter
