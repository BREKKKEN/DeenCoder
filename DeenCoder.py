import os
import pyttsx3
from colorama import Fore           
import os
import datetime
import platform 

oname = platform.system()

now = datetime.datetime.now()

if oname.lower() == 'windows':
    ()
else:
    print('Your system is not compatable with this software.')
    while True:
        print('You can exit at anytime.')
        pass

print(f""" _____    ______   ______   _   _    _____    ____    _____    ______   _____  
|  __ \  |  ____| |  ____| | \ | |  / ____|  / __ \  |  __ \  |  ____| |  __ \  login time: {"%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)}
| |  | | | |__    | |__    |  \| | | |      | |  | | | |  | | | |__    | |__) | email the creator @: deencodergit@gmail.com
| |  | | |  __|   |  __|   | . ` | | |      | |  | | | |  | | |  __|   |  _  /  github - https://github.com/BREKKKEN/DeenCoder
| |__| | | |____  | |____  | |\  | | |____  | |__| | | |__| | | |____  | | \ \  Developed by username8bit on github
|_____/  |______| |______| |_| \_|  \_____|  \____/  |_____/  |______| |_|  \_\ [v0.2.3]
------------------------------------------------------------------------------------------------------------------------------""")

t1 = 'DeenCoder-Main'
t2 = 'DeenCoder-Morse to English'
t3 = 'DeenCoder-English to Morse' 

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', '+': '.-.-.', '=': '-...-',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', '!': '-.-.--', ')': '-.--.-', '"': ".-..-.",
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', '/': '-..-.', '(': '-.--.', ':': '---...',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  '?': '..--..', '@': '.--.-.', ';': '-.-.-.',
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
    return "".join(english)  

def main():
    while True:
        os.system(f'title {t1}')
        print("")
        print('DeenCoder - Please choose 1/2/3/4/5 - Please note that DeenCoder is still in the beta stages!')
        response = input("""[1] to Convert Morse Code to English
[2] to Convert English to Morse Code
[3] to Print a Morse Code Chart
[4] to Print Help/Credits
[5] to Exit DeenCoder
[?~] """)
        if response == "1":
         os.system(f'title {t2}')
         print("")
         print('example: -.. . . -. -.-. --- -.. . .-.> DeenCoder')
         print("Enter Morse code (with a space after each code): ")
         morse = input("~> ")
         print("")
         english = morse_to_english(morse)
         print('')
         print(Fore.GREEN + '### English version ###')
         print(Fore.GREEN + english)
         print(Fore.GREEN + '### English version ###')
         print(Fore.WHITE + '')
         print("")
         line1 = [english]
         with open('line1.txt', 'w') as f:
             f.writelines(line1)
         print(Fore.YELLOW, '')
         print('saved to line1.txt')
         print(Fore.WHITE, '')
         yn = input('Play message (y/n): ')
         if yn.lower() == 'y':
             print("")
             print(Fore.YELLOW + f"saying - {english}")
             print(Fore.WHITE + "")
             text_speech = pyttsx3.init()
             text_speech.say(english)
             text_speech.runAndWait()
         if yn.lower() == 'n':
             ()
         else:
             ()

        elif response == "2":
         os.system(f'title {t3}')
         print("")
         print('example: DeenCoder> -.. . . -. -.-. --- -.. . .-.')
         print("Enter English text: ")
         english = input("~> ").upper()
         print("")
         morse = english_to_morse(english)
         print('')
         print(Fore.GREEN + '### Morse Code version ###')
         print(Fore.GREEN + morse)
         print(Fore.GREEN + '### Morse Code version ###')
         print(Fore.WHITE + '')
         line2 = [morse]
         with open('line2.txt', 'w') as f:
             f.writelines(line2)
         print(Fore.YELLOW, '')
         print('saved to line2.txt')
         print(Fore.WHITE, '')
        elif response == "5":
         exit()
    
        elif response == "3":
         print(Fore.GREEN + '')
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
(      -.--.    )       -.--.-
=      -...-    ;       -.-.-.
:      ---...   "       .-..-.""")        
         print(Fore.WHITE + '')
        
        elif response == '4':
            print(Fore.YELLOW + " ")
            print("""HELP:

if a translation is blank or missing text: this happens when there are unsupported characters or unkown morse code in text you typed

all supported characters are listed in the morse code chart to acsses the morse code chart type 3 in the main menu

typing "res" or "reset" in the main menu will clear the screen/console

typing "re1" in the main menu will re-print your latest morse to english translation

typing "re2" in the main menu will re-print your latest english to morse translation

CREDITS:

Developed by username8bit on github

Colred text made using the colorama package

Text to speech made using the pyttsx3 package

Login time made using the datetime package

DeenCoder Github - https://github.com/BREKKKEN/DeenCoder

email the creator @- deencodergit@gmail.com """)
            print(Fore.WHITE + " ")

        elif response.lower() == 'res' or response.lower() == 'reset':
            os.system('cls')
        
        elif response.lower() == 're1':
            n = open('line1.txt')
            N = n.read()
            print(Fore.YELLOW, '')
            print('latest morse to english translation(English text):')
            print('', N)
            print(Fore.WHITE, '')
        
        elif response.lower() == 're2':
            n2 = open('line2.txt')
            n2r = n2.read()
            print(Fore.YELLOW, '')
            print('latest english to morse translation(morse code text):')
            print('', n2r)
            print(Fore.WHITE, '')

        elif response == '':
          ()

        else:
           print(" ")
           print(Fore.RED + 'Please Enter a valid oporation!')
           print(Fore.WHITE + '')
   
if __name__ == "__main__":
    main()