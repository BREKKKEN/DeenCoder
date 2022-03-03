import os
print(""" _____    ______   ______   _   _    _____    ____    _____    ______   _____  
|  __ \  |  ____| |  ____| | \ | |  / ____|  / __ \  |  __ \  |  ____| |  __ \ 
| |  | | | |__    | |__    |  \| | | |      | |  | | | |  | | | |__    | |__) |
| |  | | |  __|   |  __|   | . ` | | |      | |  | | | |  | | |  __|   |  _  /  -.. . . -. -.-. --- -.. . .-.
| |__| | | |____  | |____  | |\  | | |____  | |__| | | |__| | | |____  | | \ \  
|_____/  |______| |______| |_| \_|  \_____|  \____/  |_____/  |______| |_|  \_\ [v0.1]""")


t1 = 'DeenCoder-Main'
t2 = 'DeenCoder-Morse to English'
t3 = 'DeenCoder-English to Morse'

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key


def english_to_morse(message):
    morse = []  
    for char in message:
        if char in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[char])
    return " ".join(morse)


def morse_to_english(message):
    message = message.split(" ")
    english = []  
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)


def main():
    while True:
        os.system(f'title {t1}')
        print("")
        print('Please choose 1/2/3 or type 4 to list a morse code chart')
        response = input("""[1] Convert Morse Code to English
[2] Convert English to Morse Code
[3] Exit DeenCoder 
[?~] """).upper()
        if response == "1" or response == "2" or response == '3' or response == '4':
            break

    if response == "1":
        os.system(f'title {t2}')
        print("")
        print('example: .... . .-.. .-.. --- > Hello')
        print("Enter Morse code (with a space after each code): ")
        morse = input("> ")
        print("")
        english = morse_to_english(morse)
        print('')
        print("### English version ###")
        print(english)
        print("### English version ###")
        print('')
        main()

    elif response == "2":
        os.system(f'title {t3}')
        print("")
        print('example: Hello > .... . .-.. .-.. ---')
        print("Enter English text: ")
        english = input("> ").upper()
        print("")
        morse = english_to_morse(english)
        print('')
        print("### Morse Code version ###")
        print(morse)
        print("### Morse Code version ###")
        print('')
        main()
    
    elif response == "3":
        exit()
    elif response == "4":
        print("")
        print("""A	.-	B	-...
C	-.-.	D	-..
E	.	F	..-.
G	--.	H	....
I	..	J	.---
K	-.-	L	.-..
M	--	N	-.
O	---	P	.--.
Q	--.-    R	.-.
S	...	T	-
U	..-	V	...-
W	.--	X	-..-
Y	-.--	Z	--..
0	-----	1	.----
2	..---	3	...--
4	....-	5	.....
6	-....	7	--...
8	---..	9	----. """)
        main()

if __name__ == "__main__":
    main()
