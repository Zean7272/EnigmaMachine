from consts import *
class Rotor:

    def __init__(self, wiring, notch):
        self.left = alpha_0
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=0):
        for i in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_letter(self, let):
        pos = self.left.find(let)
        self.rotate(pos)

    def show_top(self):
        return self.left[0]