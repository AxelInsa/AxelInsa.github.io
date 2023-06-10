---
title: CTFs | 404CTF2023 | Reverse | Le Divin Crackme 
author: Stillwolfing
date: 2023-06-10
categories: ['CTFs', '404CTF2023', 'Reverse']
tags: ['CTFs', '404CTF2023', 'Reverse']
permalink: /CTFs/404CTF2023/reverse/le_divin_crackme
---

## Context

![context](/assets/img/CTFs/404CTF2023/reverse/le_divin_crackme/context.png)

We are given the executable "divin-crackme".

We have to find the compiler used, the function used to compare the user input to the password and the password.

![mdp_fail](/assets/img/CTFs/404CTF2023/reverse/le_divin_crackme/mdp_fail.png)


Let's analyze the executable using Ghidra.

Ghidra indicates us that the gcc compiler was used.

Here is the main function:

![main](/assets/img/CTFs/404CTF2023/reverse/le_divin_crackme/main.png)

The function asks the user to enter the password.

Then it compares the first part of the input to "L4_pH1l0so", the second part to "Ph13_d4N5_" and the 3rd part of the input to "l3_Cr4cKm3".

So, the password is "L4_pH1l0soPh13_d4N5_l3_Cr4cKm3".

The function used to compare the user input to the password is "strncmp"

![mdp_success](/assets/img/CTFs/404CTF2023/reverse/le_divin_crackme/mdp_success.png)

Flag format: 404CTF{compilateur:fonction:mot_de_passe}

So, the flag is: 404CTF{gcc:strncmp:L4_pH1l0soPh13_d4N5_l3_Cr4cKm3}

I hope you enjoyed this writeup 😄 !
