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

def printSequence():
    print("Please put in an English letter: ")
    letter = sys.stdin.readline().rstrip()
    for key, value in morseDict.items():
        if letter == key:
            print( "'" + letter + "' is " + morseDict.get(key))

def printLetter():
    print("Please put in a Morse Code Sequence: ")
    sequence = sys.stdin.readline().rstrip()
    for key, value in morseDict.items():
        if sequence == value:
            print("this translates to: " + key)
            return

    print("this translates to: does not exist")



def main():
    print("Do you want to convert a letter/number to morse(1), a morse code sequence to a letter(2), a word/sentence(3),"
          "or morse to word/sentence(4)?")
    answer = int(sys.stdin.readline())
    if answer == 1:
        printSequence()
    elif answer == 2:
        printLetter()
    elif answer == 3:
        wordToMorse()
    else:
        morseToEnglish()


main()

