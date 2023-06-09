---
title: CTFs | 404CTF2023 | Forensic | Le Mystère du roman d'amour
author: Stillwolfing
date: 2023-06-09
categories: ['CTFs', '404CTF2023', 'Forensic']
tags: ['CTFs', '404CTF2023', 'Forensic']
permalink: /CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour
---

## Context

![context](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/context.png)

We are given fichier-etrange.swp.

The goal is to find:
- the PID of the crashed processus
- the path to the file
- the username 
- the machine name
- the content of the txt file.

## Resolution

A SWP file, also known as a Swap file, is a type of temporary file used to supplement the system's physical memory (RAM) by providing additional virtual memory.

In the context of the Vim text editor, a .swp file is a temporary file created by Vim to store changes made to a file while it is being edited. When you open a file in Vim, it creates a corresponding .swp file in the same directory to serve as a backup and recovery mechanism.

Running the file command, we can recover a lot of informations:

![file](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/file.png)

We have:
- the PID -> 168
- the username -> jacqueline
- the hostname -> aime_ecrire
- the path to the file -> ~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt

We still have to get the content of the txt file.

We can recover the file by running: ```vim -r fichier-etrange.swp```

We press Enter and save the file (:wq). We cannot save the file because the file structure does not exist:

![error](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/error.png)

We create the right file structure and do it again.

Now we have the file extracted:

![extract](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/extract.png)

It's a PNG image:

![brouillon.txt](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/brouillon.txt.png)

Nothing interesting on it:

![brouillon](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/brouillon.png)

I used Aperi'solve to check whether the image hide something.

It's a qr code:

![qr](/assets/img/CTFs/404CTF2023/forensic/le_mystere_du_roman_d_amour/qr.png)

It gives us the text to enter in the flag.

Final flag: 404{168-~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt-jaqueline-aime_ecrire-3n_V01L4_Un_Dr0l3_D3_R0m4N}

I hope you liked this writeup 🤗 !






