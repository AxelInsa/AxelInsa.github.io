---
title: 'CTFs | AmateursCTF2023 | Web | Waiting an Eternity'
author: Stillwolfing
date: 2023-07-18
categories: ['CTFs', 'AmateursCTF2023', 'Web']
tags: ['CTFs', 'AmateursCTF2023', 'Web']
permalink: /CTFs/AmateursCTF2023/web/waiting-an-eternity
---

# Statement

![statement](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/context.png)

# Resolution

On the home page, there is just this message. Nothing else.

![home](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/home.png)

In the response of the main page, there is a "refresh" header with a url inside. 

![response_header](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/response_header.png)

On this new page, there is this message.

![secret-site](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/secret-site.png)

There is a "time" cookie set.

![time_header](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/time_header.png)

If I set the value of the cookie to 0 and refresh the page, the message changes.

![change_time_header](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/change_time_header.png)

Since we have to wait for an "eternity", I set the "time" cookie to a high negative value (-1e1000000) and refresh the page.

We get the flag !!

![flag](/assets/img/CTFs/AmateursCTF2023/web/waiting-an-eternity/flag.png)

This challenge is an introduction to the concept of headers and cookies. I hope you have learned something with this writeup 😊.








