---
title: CTFs | 404CTF2023 | Osint |  Le Tour de France
author: Stillwolfing
date: 2023-06-11
categories: ['CTFs', '404CTF2023', 'Osint']
tags: ['CTFs', '404CTF2023', 'Osint']
permalink: /CTFs/404CTF2023/osint/le_tour_de_france
---

## Context

![context](/assets/img/CTFs/404CTF2023/osint/le_tour_de_france/context.png)

We are given this image:

![image](/assets/img/CTFs/404CTF2023/osint/le_tour_de_france/Le_Tour_de_France.png)

We have to find the location of the panel.

## Resolution

It seems that we are at a freeway exit. On the right panel we can see that we are going to the A6 freeway and on the left panel to the A5 freeway. I searched a lot to find the location using these two informations and the directions on the panels.

Then I realised I could use the E17 E21 information because it's european routes.

This what I get by searching it:

![e17_e21](/assets/img/CTFs/404CTF2023/osint/le_tour_de_france/e17_e21.png)

![panel](/assets/img/CTFs/404CTF2023/osint/le_tour_de_france/panel.png)

Looking at the url, we can retrieve the coordinates needed to create the flag.

![url](/assets/img/CTFs/404CTF2023/osint/le_tour_de_france/url.png)

lag: 404CTF{47.01,4.86} (it's not rounded but truncated btw)

I hope you like this writeup. Have a great day 😉

























