from consts import *
class Plugboard:

    def __init__(self, pairs):
        self.left = alpha_0
        self.right = alpha_0
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.right[signal]

        signal = self.left.find(letter)
        print(f"plugboard forward: {self.left[signal]}")
        return signal

    def backward(self, signal):
        letter = self.left[signal]

        signal = self.right.find(letter)
        print(f"plugboard backward: {self.right[signal]}")
        return signal

# PB = Plugboard(["AR", "XS", "PO"])
# print(PB.forward(0))
# print(PB.backwards(17))