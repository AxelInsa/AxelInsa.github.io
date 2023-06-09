---
title: CTFs | 404CTF2023 | Forensic | Pêche au livre 
author: Stillwolfing
date: 2023-06-09
categories: ['CTFs', '404CTF2023', 'Forensic']
tags: ['CTFs', '404CTF2023', 'Forensic']
permalink: /CTFs/404CTF2023/forensic/peche_au_livre
---

## Context

![context](/assets/img/CTFs/404CTF2023/forensic/peche_au_livre/context.png)

We are given a network packet capture, let's open it with Wireshark.

There are 5 TCP conversations on port 80, It must be a web server:

![conversations](/assets/img/CTFs/404CTF2023/forensic/peche_au_livre/conversations.png)


Looking at the Protocol Hierarchy, we can confirm that HTTP is used:

![protocols](/assets/img/CTFs/404CTF2023/forensic/peche_au_livre/protocols.png)

Looking at the conversations (Follow TCP stream), we can see that several images are transfered from the server to the client.

Let's download them (File > Export Objects > HTTP).

Let's take a look at them:

![karl_marx](/assets/img/CTFs/404CTF2023/forensic/peche_au_livre/karl_marx.jpg)

![karlmarx_fancam.jpg](/assets/img/CTFs/404CTF2023/forensic/peche_au_livre/karlmarx_fancam.jpg)

![Hegel-sensei-uwu.png](/assets/img/CTFs/404CTF2023/forensic/peche_au_livre/Hegel-sensei-uwu.png)

We've got the flag 🎉 !!

We can use an online OCR (Optical Character Recognition) to retrieve the flag:

```404CTF{345Y_W1r35h4rK}```

I hope you enjoyed this writeup 😊 !











