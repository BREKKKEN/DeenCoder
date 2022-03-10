import os
print(""" _____    ______   ______   _   _    _____    ____    _____    ______   _____  
|  __ \  |  ____| |  ____| | \ | |  / ____|  / __ \  |  __ \  |  ____| |  __ \ 
| |  | | | |__    | |__    |  \| | | |      | |  | | | |  | | | |__    | |__) |
| |  | | |  __|   |  __|   | . ` | | |      | |  | | | |  | | |  __|   |  _  /  -.. . . -. -.-. --- -.. . .-.
| |__| | | |____  | |____  | |\  | | |____  | |__| | | |__| | | |____  | | \ \  
|_____/  |______| |______| |_| \_|  \_____|  \____/  |_____/  |______| |_|  \_\ [v0.1.5]""")

t1 = 'DeenCoder-Main'
t2 = 'DeenCoder-Morse to English'
t3 = 'DeenCoder-English to Morse'

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', '+': '.-.-.',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', '!': '-.-.--', ')': '-.--.-',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', '/': '-..-.', '(': '-.--.',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  '?': '..--..', '@': '.--.-.',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '+': '.-.-.', '&': '.-...'}


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
        print('DeenCoder - Please choose 1/2/3/4')
        response = input("""[1] to Convert Morse Code to English
[2] to Convert English to Morse Code
[3] to Print a Morse Code Chart
[4] to Exit DeenCoder
[?~] """)
        if response == "1":
         os.system(f'title {t2}')
         print("")
         print('example: .... . .-.. .-.. --- > Hello')
         print("Enter Morse code (with a space after each code): ")
         morse = input("~> ")
         print("")
         english = morse_to_english(morse)
         print('')
         print("### English version ###")
         print(english)
         print("### English version ###")
         print('')

        elif response == "2":
         os.system(f'title {t3}')
         print("")
         print('example: Hello > .... . .-.. .-.. ---')
         print("Enter English text: ")
         english = input("~> ").upper()
         print("")
         morse = english_to_morse(english)
         print('')
         print("### Morse Code version ###")
         print(morse)
         print("### Morse Code version ###")
         print('')
    
        elif response == "4":
         exit()
    
        elif response == "3":
         print(" ")
         print("""A	.-	B	-...
C	-.-.	D	-..
E	.	F	..-.
G	--.	H	....
I	..	J	.---
K	-.-	L	.-..
M	--	N	-.
O	---	P	.--.
Q	--.-	R	.-.
S	...	T	-
U	..-	V	...-
W	.--	X	-..-
Y	-.--	Z	--..
0	-----	1	.----
2	..---	3	...--
4	....-	5	.....
6	-....	7	--...
8	---..	9	----.
.      .-.-.-   ,       --..--
?      ..--..   /       -..-.
!      -.-.--   +       .-.-.
@      .--.-.   &       .-...
(      -.--.    )       -.--.-""")        
        
        elif response == '':
          ()

        else:
           print(" ")
           print("Please Enter a valid oporation")
   
if __name__ == "__main__":
    main()