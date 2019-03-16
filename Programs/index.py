import wave
import math
import array


data = array.array('h')

def gen_audio(string, name="lesson.wav"):
    global data
    data = array.array('h')
    file = wave.open("static/audio/" + name, "w")
    file.setnchannels(1)
    file.setsampwidth(2)
    file.setnframes(2822400)
    file.setframerate(44100)
    file.setcomptype("NONE", "Uncompressed")
    freq = 440

    letters = {"a": ".-",
               "b": "-...",
               "c": "-.-.",
               "d": "-..",
               "e": ".",
               "f": "..-.",
               "g": "--.",
               "h": "....",
               "i": "..",
               "j": ".---",
               "k": "-.-",
               "l": ".-..",
               "m": "--",
               "n": "-.",
               "o": "---",
               "p": ".--.",
               "q": "--.-",
               "r": ".-.",
               "s": "...",
               "t": "-",
               "u": "..-",
               "v": "...-",
               "w": ".--",
               "x": "-..-",
               "y": "-.--",
               "z": "--..",
               " ": " "}

    for s in string:
        for ch in letters[s]:
            dot(3)
            if ch == ".":
                dot(1)
                print(".", end="")
            elif ch == "-":
                dot(3)
                print("-", end="")
            elif ch == " ":
                print(" ", end="")
                adot(1)
            print(" ", end="")
            adot(1)
        print("  ", end="")
        adot(2)
    print("")
    
    file.writeframes(data.tostring())
    file.close()
    
def dot(n):
    global data
    for i in range(n * 4410):
        sample = 20000
        sample *= math.sin((math.pi * 2 * (i % int(44100 / 440)) / int(44100 / 440)) * 2)  
        data.append(int(sample))

def adot(n):
    global data
    for i in range(n * 5010):
        data.append(0)


