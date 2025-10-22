def run_enigma(message, KB, PB, RT_1, RT_2, RT_3, RF):
    while True:
        output = ''
        for letter in message:
            signal = KB.forward(letter)
            print(signal)
            signal = PB.forward(signal)
            print(signal)
            signal = RT_1.forward(signal)
            print(signal)
            signal = RT_2.forward(signal)
            print(signal)
            signal = RT_3.forward(signal)
            print(signal)
            signal = RF.reflect(signal)
            print(signal)
            signal = RT_3.backward(signal)
            print(signal)
            signal = RT_2.backward(signal)
            print(signal)
            signal = RT_1.backward(signal)
            print(signal)
            signal = PB.backward(signal)
            print(signal)
            letter = KB.backward(signal)
            print(letter)
            RT_3.rotate(1)
            if RT_3.show_top() == RT_3.notch:
                RT_2.rotate(1)
            if RT_2.show_top() == RT_2.notch:
                RT_1.rotate(1)
            if RT_1.show_top() == RT_1.notch:
                RT_1.rotate(1)
                RT_2.rotate(1)
                RT_3.rotate(1)
            output = output + letter
        return output
