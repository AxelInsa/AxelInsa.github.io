---
title: CTFs | FCSC2023 | Hardware | Fibonacci
author: Stillwolfing
date: 2023-04-30
categories: [CTFs, FCSC2023, Hardware]
tags: [CTF, FCSC, ASM]
permalink: /CTFs/FCSC2023/hardware/fibonacci
---

Here is the context:

![context](/assets/img/CTFs/FCSC2023/hardware/fibonacci/context.png)

This chall is an introduction to assembly code. Assembly code is important to know in reverse engineering or pwn challenges.

This challenge uses the same machine as this one : [FCSC 2023: Comparaison](/CTFs/FCSC2023/Intro/comparaison/).

We are given:
- the code of the machine (machine.py)
- a code to translate the assembly code into hex format in order to send it to the server (assembly.py)
- the code present on the server (challenge.py)

In this challenge, we have to compute the fibonacci sequence.

Here is the python code I created:

```python
from assembly import assembly

code = """

; Initialize variables
MOV R3, #0
MOV R4, #1

MOV R0, #0   ; first number in sequence
MOV R1, #1   ; second number in sequence

loop:
    CMP R5, R3
    JZA done
    SUB R5, R5, R4

    ADD R2, R0, R1
    MOV R0, R1  
    MOV R1, R2
    JA loop  

done:

STP
"""

code = code.split("\n")

print(assembly(code))
```

R5 contains the number of the fibonacci sequence we want to compute.

R0 and R1 contains the first two numbers of the sequence (0 and 1).

R2 is used to store the sum of the two numbers.

We compare R5 and R3 (which is 0) and jump to the label "done" if they are equal.

If they are different, we subtract R4 (which is 1) from R5 and jump to the label "loop".

In the loop, we add R0 and R1 and store the result in R2.

Then, we move the value of R1 to R0 and the value of R2 to R1.

Finally, we jump to the label "loop".

Let's send it to the server:

![flag](/assets/img/CTFs/FCSC2023/hardware/fibonacci/flag.png)

We get the flag 🎉 !

