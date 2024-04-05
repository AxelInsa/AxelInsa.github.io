---
title: 'CTFs | CTF-inter-INSA2024 | Realist | Admin Files'
author: bipboup
date: 2024-04-05
categories: ['CTFs', 'CTF-inter-INSA2024', 'Realist']
tags: ['CTFs', 'CTF-inter-INSA2024', 'Realist']
permalink: /CTFs/CTF-inter-INSA2024/realist/admin_files
---

Let's run nmap on the target:

![nmap](/assets/img/CTFs/CTF-inter-INSA2024/realist/admin_files/nmap.png)

There are 2 ports open:
* 22 -> ssh
* 80 -> website

On the web site is run with the elfinder software which is an open-source file manager for web.

![elfinder](/assets/img/CTFs/CTF-inter-INSA2024/realist/admin_files/elfinder.png)

There is one file on the website named CredsE.txt which contains credentials encoded with ROT.

![creds_rot](/assets/img/CTFs/CTF-inter-INSA2024/realist/admin_files/creds_rot.png)

We decode it with Cyberchef and get the debian credentials:

![cyberchef](/assets/img/CTFs/CTF-inter-INSA2024/realist/admin_files/cyberchef.png)

We connect as debian and get the user flag.

![user_flag](/assets/img/CTFs/CTF-inter-INSA2024/realist/admin_files/user_flag.png)


debian can /usr/bin/python with sudo permissions so the privesc is quite easy.

![root_flag](/assets/img/CTFs/CTF-inter-INSA2024/realist/admin_files/root_flag.png)

We've got the root flag 🎉
