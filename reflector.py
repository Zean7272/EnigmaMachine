from consts import *
class Reflector:

    def __init__(self, wiring):
        self.left = alpha_0
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        print(f"letter in: {letter}")
        signal = self.left.find(letter)
        print(f"letter out: {self.left[signal]}")
        return signal