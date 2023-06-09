---
title: CTFs | 404CTF2023 | Steganography | Odobenus Rosmarus
author: Stillwolfing
date: 2023-06-09
categories: ['CTFs', '404CTF2023', 'Steganography']
tags: ['CTFs', '404CTF2023', 'Steganography']
permalink: /CTFs/404CTF2023/steganography/odobenus_rosmarus
---

## Context

![context](/assets/img/CTFs/404CTF2023/steganography/odobenus_rosmarus/context.png)

The text is:

```txt
Ce soir je Célèbre Le Concert Electro Comme Louis Et Lou. Comme La nuit Commence Et Continue Clairement, Et Clignote Lascivement il Chasse sans Chausser En Clapant Encore Classiquement Les Cerclages du Clergé. Encore Car Encore, Louis Lou Entamant Longuement La Lullabile En Commençant Le Cercle Exhaltant de Club Comique Cannais Et Clermontois.
```

## Resolution

The title "Odobenus Rosmarus" is the scientific name for "morse". So, we can guess we have to find Morse code in the text.

Looking at the text, we can notice that there words beginning with C, L, and E begins with an uppercase.

Since we have to find Morse code, we can guess that C stands for "court" (short in frensh), L stands for "long" (same in frensh) and E stands for "espace" (space in frensh).

We have "CCLCECLELCLCECCECLCCECECLCCECELLELLLECLCECCCEC"

The Morse code is "..-. .- -.-. .. .-.. . .-.. . -- --- .-. ... .". We just have to decode it.

## Implementation

Here is my implementation to solve this challenge. I extract the uppercases from the text then I convert them to standard morse format (C -> ".", L -> "-", E -> " "). To finish, I decode the morse code to get the content of the flag.

```python
def decode_morse_code(morse_code: str) -> str:
    """
    Description: Decode a morse code message
    Input: morse_code (string)
    Output: decoded_message (string)
    """
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
    words = morse_code.split(' / ')
    decoded_message = ''
    for word in words:
        characters = word.split()
        for char in characters:
            if char in morse_dict:
                decoded_message += morse_dict[char]
        decoded_message += ' '
    return decoded_message.strip()

text = "Ce soir je Célèbre Le Concert Electro Comme Louis Et Lou. Comme La nuit Commence Et Continue Clairement, Et Clignote Lascivement il Chasse sans Chausser En Clapant Encore Classiquement Les Cerclages du Clergé. Encore Car Encore, Louis Lou Entamant Longuement La Lullabile En Commençant Le Cercle Exhaltant de Club Comique Cannais Et Clermontois."

# Extract the majuscules
maj = ""
for c in text:
    if c.isupper():
        maj += c
print("Majuscules: ", maj)

# Convert from CLE to morse code
morse = ""
for c in maj:
    if c == "C":
        morse += "."
    elif c == "L":
        morse += "-"
    elif c == "E":
        morse += " "
print("Morse: ", morse)

# Decode the morse code
message = decode_morse_code(morse)
print("Message: ", message)
```

Output:

![flag](/assets/img/CTFs/404CTF2023/steganography/odobenus_rosmarus/flag.png)

The flag is: 404CTF{FACILELEMORSE}
