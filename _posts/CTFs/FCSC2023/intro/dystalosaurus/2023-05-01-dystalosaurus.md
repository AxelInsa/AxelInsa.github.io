---
title: CTFs | FCSC2023 | Intro | Dystalosaurus
author: Stillwolfing
date: 2023-05-01
categories: [CTFs, FCSC2023, Intro]
tags: [CTF, FCSC, Intro, Hardware]
permalink: /CTFs/FCSC2023/intro/dystalosaurus
---


Here is the context:

![context](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/context.png)

We are given the capture made with Salae Logic 2 (dystalosaurus.sal)

We install Salae Logic 2 and open the capture:

![salae](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/salae.png)

By zooming it gives something like this. 

![zoom](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/zoom.png)

It seems to be only one signal, no clock.

By searching on the internet, Salae Logic 2 has analyzers to read the signal. Since there is no clock, I create an Async Serial analyzer like this:

![analyzer](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/analyzer.png)

It looks like the analyzer found text:

![words](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/words.png)

I export to TXT/CSV

![export](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/export.png)


Here is the result:

![raw-export](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/raw-export.png)


With a python script, we reconstruct the text:

[salae-csv2txt](https://github.com/kxynos/saleae-csv2text)

![text](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/text.png)

We filter to get the flag 🙂:

![flag](/assets/img/CTFs/FCSC2023/Intro/dystalosaurus/flag.png)

