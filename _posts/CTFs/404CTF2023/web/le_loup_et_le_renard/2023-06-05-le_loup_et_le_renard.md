---
title: CTFs | 404CTF2023 | Le Loup et le renard
author: Stillwolfing
date: 2023-06-05
categories: [CTFs, 404CTF2023, Web]
tags: [CTF, 404CTF, Web]
permalink: /CTFs/404CTF2023/web/le_loup_et_le_renard
---

Here is the context:

![context](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/context.png)


This challenge is made of 3 parts. Here is the first one:

![partie1_context](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/partie1_context.png)

Le texte nous indique que l'authentification est géré en front-end (côté client). En regardant le code source de la page, on peut observer le mécanisme d'authentication:

![partie1_auth](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/partie1_auth.png)

On obtient le username "admin" et le mot de passe "h5cf8gf2s5q7d".

On est redirigé vers la 2ème partie du challenge:

![partie2_context](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/partie2_context.png)

Le texte mentionne les cookies et le fait que l'authentification est faite en front-end.

Parmi les cookies se trouve un cookie isAdmin:

![partie2_cookie_unchanged](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/partie2_cookie_unchanged.png)

On change la valeur du cookie isAdmin à true et on recharge la page.

On est redirigé vers la 3ème partie du challenge:

![partie3_context](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/partie3_context.png)

En voyant le titre Redirect, j'ai pensé que la vulnérabilité était du type Execute After Redirect (EAR)

I intercepted the response with burpsuite.

![flag](/assets/img/CTFs/404CTF2023/web/le_loup_et_le_renard/flag.png)

The page is executed then we get redirected so we are able to read sensitive content.

I hope you understood this writeup 😊
