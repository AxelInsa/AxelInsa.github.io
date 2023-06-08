---
title: CTFs | 404CTF2023 | Web | L'Academie du détail
author: Stillwolfing
date: 2023-06-05
categories: [CTFs, 404CTF2023, Web]
tags: [CTFs, 404CTF2023, Web]
permalink: /CTFs/404CTF2023/web/l_academie_du_detail
---

Here is the context:

![context](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/context.png)

Here is the website main page:

![home](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/home.png)

There are 4 endpoints:
- /login -> we can connect as whoever we want as long as it's not admin
- /logout -> to disconnect
- /home -> just the home page
- /membres to see the members of the academy.

By going to the endpoint /membres we get this page:

![membres](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/membres.png)


After trying to SQLI the login form, I noticed that we have a JWT token as auth cookie:

![cookie](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/cookie.png)

By using Cyberchef, we can decode it (we can also jwt.io or just base64 decode each part):

![cyberchef_decode](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/cyberchef_decode.png)

I tried to change the value of username by "admin" and change the algorithm used for the key by "None". If the site does not verify that the good algorithm is used, it could validate the token.

![cyberchef_encode](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/cyberchef_encode.png)

I change the value of the "access-token" cookie by the new value and access the /membres endpoint.

Here we go 😃 !

![flag](/assets/img/CTFs/404CTF2023/web/l_academie_du_detail/flag.png)

I hope you understood the process. If you want to know more, dig about JWT token vulnerabilities.


