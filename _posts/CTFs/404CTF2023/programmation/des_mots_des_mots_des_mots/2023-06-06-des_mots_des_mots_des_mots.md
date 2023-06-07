---
title: CTFs | 404CTF2023 | Programmation | Des mots, des mots, des mots
author: Stillwolfing
date: 2023-06-06
categories: ['CTFs', '404CTF2023', 'Programmation']
tags: ['CTFs', '404CTF2023', 'Programmation']
permalink: /CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots
---

Here is the context:

![context](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/context.png)

Let's connect to the challenge to know more.

![nc](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/nc.png)

It seems like there will be different rules.

No need to implement anything for this one.

I implemented a function to send datas and receive the response.

```python
def send_receive(r, msg):
    r.send(msg)
    print(r.recvuntil('>> ').decode())
```

Here r is the connection made with the pwn library.

My code for Rule 0 is the following:
```python
import pwn
from functions import *


if __name__ == '__main__':

    r = pwn.remote('challenges.404ctf.fr', 30980)

    response = r.recvuntil(b'>> ').decode()
    print(response)

    send_receive(r, 'cosette')
```

We just send 'cosette'.
functions is a python file where I put my functions.

Here is the output of the code:

![rule0_output](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/rule0_output.png)

## First Rule

For the Rule 1, we need to invert the letters in the input.

Example:

if the input is 'cosette', the output of the Rule 1 is 'ettesoc'.

Here is my implementation of the Rule 1:

```python
def rule_1(msg, original):
    return msg[::-1], original
```

I completed the main code to send it to the server.

```python
msg1, original = rule_1('cosette', 'cosette')
print(msg1)
send_receive(r, msg1)
```

I add the original message to the parameter of the function and return it because we will need it for the 3rd Rule.

Output of the Rule 1:

![rule1_output](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/rule1_output.png)

## Second Rule

Alright, it gets harder.

If the number of letters in the input is even, we have to invert the first and the second part of the word.

Example:

'boat' has an even number of letters. We exchange the first and the second part of the word: 'bo', 'at' -> 'atbo'.

If the number of letters in the input is odd, we delete the letters corresponding to the central letter.

Example:

'cosette' has an odd number of letters.
'e' is the central letter ('cos', 'e', 'tte').
We delete every 'e' in the word 'cosette'.
It gives us 'costt'.

Here is my implementation of the second Rule:

```python
def is_nb_lettres_pair(msg):
    return len(msg) % 2 == 0


def rule_2(message):
    msg = message[0]
    original = message[1]
    if is_nb_lettres_pair(msg):
        part1 = msg[:len(msg) // 2]
        part2 = msg[len(msg) // 2:]
        return part2 + part1, original
    else:
        mid = msg[len(msg) // 2]
        return msg.replace(mid, ''), original
```

I added this to the main code:

```python
msg2, original = rule_2(rule_1('cosette', 'cosette'))
print(msg2)
send_receive(r, msg2)
```

Output of the second Rule:

![rule2_output](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/rule2_output.png)

## Third Rule

If the word contains less than 3 letters, we return the word without modification.

Else:

We use the original word (that was inputed in the first rule initially).

If the third letter of the word is a consonant, we shift the vowel to the left. Then we apply the rule 1 and the rule 2.

Example:
'poteau'. The third letter is 't', a consonant. So we shift the vowel on the left.

The vowel in 'poteau' are 'o', 'e', 'a', 'u'. We shift them on the left, like a loop: 'e', 'a', 'u', 'o'.

We insert the vowel back in the word: 'petauo'

We apply the first rule: 'petauo' -> 'ouatep'.

We apply the second rule: 'ouatep' -> 'tepoua'

If the third letter of the word is a vowel, we do the same process except that we shift the vowel on the right instead of left.

Example:

shift on the right: 'drapeau' -> 'drupaea'<br />
Then Rule 1: 'drupaea' -> 'aeapurd'<br />
Then Rule 2: 'aeapurd' -> 'aeaurd'

I struggled a lot with 3rd rule because I did not understand at first that we needed to apply the changes on the original word if the word contains 3 letters or more.

Here is my implementation of the Third Rule:

```python
voyelle = {'a', 'e', 'i', 'o', 'u', 'y'}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_voyelle(letter):
    return letter.lower() in voyelle


def is_consonne(letter):
    return letter.lower() not in voyelle and letter.lower() in alphabet


def get_list_voyelles(msg):
    list_voyelle = []
    for index, letter in enumerate(msg):
        if letter in voyelle:
            list_voyelle.append(index)
    return list_voyelle


def rotate_gauche(msg, list_voyelles):
    tmp = msg[list_voyelles[0]]
    for i in range(1, len(list_voyelles)):
        msg[list_voyelles[i - 1]] = msg[list_voyelles[i]]
    msg[list_voyelles[-1]] = tmp

    return msg


def rotate_right(msg, list_voyelles):
    tmp = msg[list_voyelles[-1]]
    for i in range(len(list_voyelles) - 1, 0, -1):
        msg[list_voyelles[i]] = msg[list_voyelles[i - 1]]
    msg[list_voyelles[0]] = tmp

    return msg


def rule_3(message):
    msg = message[0]
    original = message[1]

    msg = list(msg)
    
    if len(msg) < 3:
        return msg, original
    
    mot_original = ""

    for c in original:
        mot_original += c

    mot_original = list(mot_original)
    
    list_voyelles = get_list_voyelles(mot_original)
    if is_consonne(msg[2]):
        rotate_gauche(mot_original, list_voyelles)
    else:
        rotate_right(mot_original, list_voyelles)

    mot_original = ''.join(mot_original)
    msg1 = rule_1(mot_original, original)
    msg2 = rule_2(msg1)
    return msg2
```

I send it to the server:

```python
msg3, original = rule_3(rule_2(rule_1('cosette', 'cosette')))
print(msg3)
send_receive(r, msg3)
```

Output of the third rule:

![rule3_output](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/rule3_output.png)

## Fourth Rule

The 4th rule is very complex to understand but not really harder than the third one.

Here is my implementation (we use the same alphabet and voyelles variables. We use the same functions is_consonne and is_voyelle functions):

```python
from collections import Counter

def find_last_voyelle(code):
    while 1:
        if chr(code).lower() in voyelle:
            return code
        code -= 1


def get_sum(mot, count):
    s = 0
    for i in range(count - 1, -1, -1):
        if mot[i].lower() in voyelle:
            s += ord(mot[i]) * (2 ** (count - i))
    return s


def insert_letter(mot, count):
    vp = find_last_voyelle(ord(mot[count]))  # Previous vowel
    #s = get_sum(mot, count)
    s = sum([ord(mot[i]) * (2 ** (count - i)) * (int(is_voyelle(mot[i]))) for i in range(count - 1, -1, -1)])
    a = ((vp + s) % 95) + 32
    mot.insert(count + 1, chr(a))



def evaluate_and_insert(mot, count):
    if is_consonne(mot[count]):
        insert_letter(mot, count)


def insert_characters(word, original):
    mot = list(word)
    count = 0
    while count < len(mot):
        evaluate_and_insert(mot, count)
        count += 1
    
    return ''.join(mot)


def sort_word(word):
    # Count character occurrences
    char_counts = Counter(word)
    #print(char_counts)

    # Sort characters by occurrences (descending) and ASCII codes (ascending)
    sorted_chars = sorted(char_counts.keys(), key=lambda c: (-char_counts[c], ord(c)))

    # get the right number of occurences for each character
    sorted_chars = [c for c in sorted_chars for _ in range(char_counts[c])]

    # Build the sorted word
    sorted_word = ''.join(sorted_chars)

    return sorted_word


def rule_4(message):
    msg = message[0]
    original = message[1]
    result = insert_characters(msg, original)
    return sort_word(result)
```

In the insert_characters function, we iterate over the letters of the word. We insert a new character if the letter is a consonant.

To insert a word, we need to perform several operations.

First we need to find the ascii code of the last vowel in the alphabet preceding our letter. We name this variable 'vp'.

Then 

Example: If our letter is 's', the last voyelle is 'o' so we return the ascii code of 'o'.

I get the ascii code of the last vowel with the find_last_voyelle function.

Then if the letter is a vowel, I calculate this sum:

s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))

For each letter before the current one, we calculate a{i}*2^(n-i) with a{i} the ascii code of the letter at index i.

The ascii code of the new letter is obtained with this operation:

a = ((vp + s) % 95) + 32

We insert the new character in our word.


In the sort_word function, we sort the letters in the word obtained from the insert_characters function. (number of occurences of a letter in descending order and ASCII code in ascending order in case of draw).

I defined a rules function to apply all rules:

```python
def rules(msg, original):
    msg = rule_4(rule_3(rule_2(rule_1(msg, original))))
    return msg
```

I added the code to the main:

```python
msg4 = rules('cosette', 'cosette')
print(msg4)
r.sendline(bytes(msg4, 'utf-8'))
response = r.recvuntil(b'>>').decode()
print(response)
```

I did not use the send_receive function because i need the output for the last challenge.

Here is the output of the Fourth Rule:

![rule4_output](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/rule4_output.png)

## Last Challenge

We are given a text, we need to translate each word using the rules implemented.

Here is my implementation to do it:

```python
import re
    response = re.findall(r'\{.*\}', response)[0]
    response = response.strip('}').strip('{')


    resp = response.split(' ')
    
    resp = [rules(word, word) for word in resp]
    resp = ' '.join(resp)

    r.sendline(bytes(resp, 'utf-8'))

    response = r.recvuntil(b'}').decode()
    print(response)
```

I extract the text from the response.<br />
For each word, I apply the rules function to translate the word.

Then I join every word of my list of words with spaces and send it to the server.

Here the output:

![flag](/assets/img/CTFs/404CTF2023/programmation/des_mots_des_mots_des_mots/flag.png)

We've got the flag !!!
