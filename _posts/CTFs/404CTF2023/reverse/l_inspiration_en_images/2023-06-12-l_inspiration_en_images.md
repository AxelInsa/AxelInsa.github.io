---
title: CTFs | 404CTF2023 | Reverse | L'Inspiration en images
author: Stillwolfing
date: 2023-06-12
categories: ['CTFs', '404CTF2023', 'Reverse']
tags: ['CTFs', '404CTF2023', 'Reverse']
permalink: /CTFs/404CTF2023/reverse/l_inspiration_en_images
---

## Context

![context](/assets/img/CTFs/404CTF2023/reverse/l_inspiration_en_images/context.png)

We are given an executable that creates a painting.

Here is the painting:

![painting](/assets/img/CTFs/404CTF2023/reverse/l_inspiration_en_images/painting.png)

On the screen, we only see the bottom right of the painting. In fact the painting is entirely black. We can discover the content with the cursor. It's like if it's dark and the cursor is a flashlight. Here my cursor is in the bottom right to take the screen shot.

We have to find the color in the background of the painting.

## Resolution

I analyzed the executable with Ghidra.

The main function is long with a lot of variables. We will not analyze everything.

Line 62, the window is create:

![window](/assets/img/CTFs/404CTF2023/reverse/l_inspiration_en_images/window.png)

Line 186, the "Clear Color" is defined. It's the default of the window, before adding things to it. It is the background color we are looking for.

![color](/assets/img/CTFs/404CTF2023/reverse/l_inspiration_en_images/color.png)

In hex: 0x3e4ccccd,0x3e99999a,0x3e99999a,0x3f800000

In float: 0.2, 0.3, 0.3, 1

Flag: 404CTF{vec4(0.2,0.3,0.3,1)}
