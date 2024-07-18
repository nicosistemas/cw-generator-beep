import os
import time

caracteres = {
   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
   '8': '---..', '9': '----.', ' ': '/'
}

def play_morse_code(morse_code):
   for char in morse_code:
       if char == '.':
           #os.system('beep -f 1000 -l 400') # beep corto alter
           os.system('play -n synth %s sin %s' % (0.1,700))
       elif char == '-':
           os.system('play -n synth %s sin %s' % (0.3,700))
           #os.system('beep -f 1000 -l 800') # beep largo alter
       else:
           # Pausa entre caracteres
           time.sleep(0.5)
          
def generate_morse_code(text):
   morse_code = ''
   for char in text.upper():
       if char in caracteres:
           morse_code += caracteres[char] + ' '
   return morse_code

# Generador de codigo segun input
text = input("Enter codigo: ")
morse_code = generate_morse_code(text)

# Reproductor audio codigo
play_morse_code(morse_code)
