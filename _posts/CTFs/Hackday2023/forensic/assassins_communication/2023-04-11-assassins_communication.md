---
title: CTFs | HackDay2023 | Forensic | Assassins Communication
author: Stillwolfing
date: 2023-04-11
categories: [CTFs, HackDay2023, Forensic]
tags: [CTFs, HackDay2023, Forensic, Steganography]
permalink: /CTFs/Hackday2023/forensic/assassins_communication
---

Here is the context:

![context](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/context.png)

We have got a wireshark capture named leak.pcapng

I used binwalk on the capture to see if it contains something:

![binwalk](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/binwalk.png)

Here is what we have got:

![binwalk_result](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/binwalk_result.png)

The flag.txt file is empty and the zip file is password protected

![binwalk_result2](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/binwalk_result2.png)

So i decided to crack it !

![john](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/ohn.png)
Well... I've got nothing.

Let's take a look at the wireshark capture.
Looking at the HTTP conversation, I see that there is an image in the conversation that is in plain text.

![wireshark](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/wireshark.png)

I saved it (put the data in raw first)

![raw](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/raw.png)

And I opened it

![image](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/image.jpg)

Let's try to run steghide on this image.

![steghide](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/steghide.png)

It's password protected. Let's try to brute force it with stegseek:

![stegseek](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/stegseek.png)

We've got the zip password ! (aBqw7FB0f3VqTZrW)

Let's open the zip file.

![flag](/assets/img/CTFs/Hackday2023/forensic/assassins_communication/flag.png)

We've got the flag, well done !!
