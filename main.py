# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

morseDict= {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': "-.-",
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p':'.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '  ',
    '.': '  ',

    #'.': '.-.-.-'

    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....--',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '10': '-----'

}

def fromLetterToMorse(index):
    #letter = sys.stdin.readline().rstrip()
    for key, value in morseDict.items():
        if index == key:
            return morseDict.get(key)

def wordToMorse():
    print("Please enter a word: ")
    word = str(sys.stdin.readline().rstrip())
    for i in word:
        print(fromLetterToMorse(i), end= ' ')

def fromMorseToLetter(index):
    for key, value in morseDict.items():
        if index == value:
            return key

def morseToEnglish():
    print("Please enter your morse sequence:")
    sequence = sys.stdin.readline().rstrip().split('  ')

    for word in sequence:
        for letter in word.split():
            print(fromMorseToLetter(letter), end= '')
        print(' ', end= '')


def main():
    print("Do you want to convert word/sentence to morse(1), or morse to word/sentence(2)?")
    answer = int(sys.stdin.readline())
    if answer == 1:
        wordToMorse()
    else:
        morseToEnglish()


main()

