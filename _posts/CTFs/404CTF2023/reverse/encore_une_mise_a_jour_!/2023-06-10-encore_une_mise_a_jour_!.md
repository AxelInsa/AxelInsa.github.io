---
title: CTFs | 404CTF2023 | Reverse | Encore une mise à jour !
author: Stillwolfing
date: 2023-06-10
categories: ['CTFs', '404CTF2023', 'Reverse']
tags: ['CTFs', '404CTF2023', 'Reverse']
permalink: /CTFs/404CTF2023/reverse/encore_une_mise_a_jour_!
---

## Context

![context](/assets/img/CTFs/404CTF2023/reverse/encore_une_mise_a_jour_!/context.png)

We are given the file "encore-une-mise-a-jour.py".

![general_code](/assets/img/CTFs/404CTF2023/reverse/encore_une_mise_a_jour_!/general_code.png)

It's just a password checker, right ?

Well here is the check function:

```python
def check(dumas, zola):
    cody = h.Bytecode(check, **dico).dis().count('I')
    print(cody)
    carmen = 0

    if dumas[36] + cody * dumas[37] + dumas[38] == 25556:
        carmen += 1
    if dumas[3] + cody * dumas[4] + dumas[5] == 19862:
        carmen += 1
    if dumas[21] + cody * dumas[22] + dumas[23] == 39570:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == 35329:
        carmen += 1
    if dumas[6] + dumas[7] + cody * dumas[8] == 67347:
        carmen += 1
    if dumas[3] + dumas[4] + cody * dumas[5] == 100914:
        carmen += 1
    if dumas[3] + cody * dumas[4] + dumas[5] == 49274:
        carmen += 1    
    if dumas[6] + cody * dumas[7] + dumas[8] == 61221:
        carmen += 1
    if dumas[36] + dumas[37] + cody * dumas[38] == 64773:
        carmen += 1
    if dumas[9] + dumas[10] + cody * dumas[11] == 49360:
        carmen += 1
    if dumas[9] + cody * dumas[10] + dumas[11] == 18857:
        carmen += 1
    if dumas[9] + cody * dumas[10] + dumas[11] == 46721:
        carmen += 1    
    if dumas[15] + dumas[16] + cody * dumas[17] == 58164:
        carmen += 1
    if dumas[15] + dumas[16] + cody * dumas[17] == 144852:
        carmen += 1
    if dumas[12] + dumas[13] + cody * dumas[14] == 147438:
        carmen += 1
    if dumas[12] + dumas[13] + cody * dumas[14] == 59202:
        carmen += 1
    if dumas[45] + cody * dumas[46] + dumas[47] == 39501:
        carmen += 1
    if dumas[12] + cody * dumas[13] + dumas[14] == 25080:
        carmen += 1
    if dumas[15] + cody * dumas[16] + dumas[17] == 27661:
        carmen += 1
    if dumas[18] + dumas[19] + cody * dumas[20] == 135810:
        carmen += 1
    if dumas[18] + cody * dumas[19] + dumas[20] == 128064:
        carmen += 1    
    if dumas[15] + cody * dumas[16] + dumas[17] == 68683:
        carmen += 1    
    if dumas[12] + cody * dumas[13] + dumas[14] == 62232:
        carmen += 1    
    if dumas[24] + cody * dumas[25] + dumas[26] == 66114:
        carmen += 1    
    if dumas[27] + cody * dumas[28] + dumas[29] == 25071:
        carmen += 1
    if dumas[6] + cody * dumas[7] + dumas[8] == 152553:
        carmen += 1    
    if dumas[6] + dumas[7] + cody * dumas[8] == 27099:
        carmen += 1
    if dumas[21] + dumas[22] + cody * dumas[23] == 54563:
        carmen += 1
    if dumas[45] + cody * dumas[46] + dumas[47] == 98325:
        carmen += 1 
    if dumas[39] + dumas[40] + cody * dumas[41] == 115125:
        carmen += 1
    if dumas[24] + cody * dumas[25] + dumas[26] == 26640:
        carmen += 1
    if dumas[21] + dumas[22] + cody * dumas[23] == 135833:
        carmen += 1
    if dumas[9] + dumas[10] + cody * dumas[11] == 122890:
        carmen += 1
    if dumas[39] + dumas[40] + cody * dumas[41] == 46239:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == 87961:
        carmen += 1
    if dumas[27] + dumas[28] + cody * dumas[29] == 144847:
        carmen += 1
    if dumas[30] + dumas[31] + cody * dumas[32] == 35402:
        carmen += 1
    if dumas[27] + dumas[28] + cody * dumas[29] == 58159:
        carmen += 1
    if dumas[3] + dumas[4] + cody * dumas[5] == 40542:
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == 42776:
        carmen += 1    
    if dumas[30] + cody * dumas[31] + dumas[32] == 57633:
        carmen += 1
    if dumas[42] + cody * dumas[43] + dumas[44] == 26019:
        carmen += 1
    if dumas[18] + dumas[19] + cody * dumas[20] == 54540:
        carmen += 1
    if dumas[18] + cody * dumas[19] + dumas[20] == 51438:
        carmen += 1
    if dumas[21] + cody * dumas[22] + dumas[23] == 98394:
        carmen += 1    
    if dumas[24] + dumas[25] + cody * dumas[26] == 51973:
        carmen += 1
    if dumas[24] + dumas[25] + cody * dumas[26] == 129373:
        carmen += 1
    if dumas[30] + dumas[31] + cody * dumas[32] == 88034:
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == 17234:
        carmen += 1
    if dumas[30] + cody * dumas[31] + dumas[32] == 143547:
        carmen += 1    
    if dumas[33] + cody * dumas[34] + dumas[35] == 43078:
        carmen += 1
    if dumas[33] + dumas[34] + cody * dumas[35] == 42770:
        carmen += 1
    if dumas[33] + cody * dumas[34] + dumas[35] == 107320:
        carmen += 1    
    if dumas[36] + dumas[37] + cody * dumas[38] == 26073:
        carmen += 1
    if dumas[33] + dumas[34] + cody * dumas[35] == 17228:
        carmen += 1
    if dumas[39] + cody * dumas[40] + dumas[41] == 27627:
        carmen += 1
    if dumas[39] + cody * dumas[40] + dumas[41] == 68649:
        carmen += 1    
    if dumas[27] + cody * dumas[28] + dumas[29] == 62223:
        carmen += 1    
    if dumas[42] + cody * dumas[43] + dumas[44] == 64719:
        carmen += 1    
    if dumas[45] + dumas[46] + cody * dumas[47] == 29161:
        carmen += 1
    if dumas[42] + dumas[43] + cody * dumas[44] == 35842:
        carmen += 1
    if dumas[36] + cody * dumas[37] + dumas[38] == 63482:
        carmen += 1    
    if dumas[42] + dumas[43] + cody * dumas[44] == 89248:
        carmen += 1
    if dumas[45] + dumas[46] + cody * dumas[47] == 72505:
        carmen += 1

    zola+zola
    return carmen == 32
```

The password has to be 48 characters long and validate 32 of the equations in the check function.

Thankfully, characters in the password are grouped by 3 for the check.

Example: Every equation where there is dumas[0], there is dumas[1] and dumas[2] and no other one. So we can calculate the value for the 3 together without worrying about other characters.

## Resolution

I created a script for the to solve each equations:

```python
import itertools

h = __import__('dis')
dico = {'adaptive': True}

cody = 518  # Set the value of cody

carmen = 0
count = 0

def checks(dumas, val):
    carmen = 0

    mid = val[0]
    end = val[1]

    if dumas[0] + cody * dumas[1] + dumas[2] == mid[0]:
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == mid[1]:
        carmen += 1

    if dumas[0] + dumas[1] + cody * dumas[2] == end[0]:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == end[1]:
        carmen += 1

    return carmen == 2


def find_pass(val):
    global count
    for i in itertools.product(range(177), repeat=3):
        if checks(i, val):
            print("".join([chr(c) for c in i]), end="")
    count += 1


find_pass(((42776,17234), (35329,87961)))
find_pass(((19862,49274), (40542,100914)))
find_pass(((61221,152553), (27099,67347)))
find_pass(((18857,46721), (49360,122890)))
find_pass(((25080,62232), (59202,147438)))
find_pass(((68683,27661), (144852,58164)))
find_pass(((128064,51438), (54540,135810)))
find_pass(((39570,98394), (135833,54563)))
find_pass(((66114,26640), (51973,129373)))
find_pass(((25071,62223), (58159,144847)))
find_pass(((57633,143547), (88034,35402)))
find_pass(((43078,107320), (17228,42770)))
find_pass(((25556,63482), (26073,64773)))
find_pass(((27627,68649), (46239,115125)))
find_pass(((26019,64719), (35842,89248)))
find_pass(((39501,98325), (72505,29161)))
```

The check function test if a triplet of value that satisfies 2 of the 4 equations that are in the original check function.

The find_pass function generate each triplet possible to find a valid triplet.

The parameters of the find_function are the values in the equation of the original check function.

Here is the output:

![password](/assets/img/CTFs/404CTF2023/reverse/encore_une_mise_a_jour_!/password.png)

The flag is 404CTF{H!Dd&N-v4r$_f0r_5p3ciaLiz3d_0pCoD3S!|12T5Y22EML8}

I hope you enjoyed this writeup. The code is overwhelming but the idea is simple.
