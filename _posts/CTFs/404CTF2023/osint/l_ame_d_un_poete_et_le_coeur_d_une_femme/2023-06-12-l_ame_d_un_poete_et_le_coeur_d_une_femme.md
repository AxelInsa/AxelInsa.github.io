---
title: CTFs | 404CTF2023 | Osint | L'âme d'un poète et le coeur d'une femme
author: Stillwolfing
date: 2023-06-12
categories: ['CTFs', '404CTF2023', 'Osint']
tags: ['CTFs', '404CTF2023', 'Osint']
permalink: /CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme
---

This challenge is in 4 parts

## First Part

### Context

![context](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/context1.png)

We have to find "Louise Colet" on social medias.

### Resolution

Looking on facebook, I found this profile.

![facebook_profile](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/facebook_profile.png)

In the "A propos" tab, we find the first flag 😊 !

![flag1](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/flag1.png)

## Second Part

### Context

![context2](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/context2.png)

Now we have to find an event organised by Louise Colet. We need to find the date of this event and the account that mention it.

So, we are looking for social medias still.

### Resolution

The facebook account we found had no more useful informations.

I looked on instagram and found this account.

![instagram_profile](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/instagram_profile.png)

On the photo, there is this text:

![instagram_photo](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/instagram_photo.png)

So the event is a literary salon organised by Louise Colet the 25 May 2023.

Flag: 404CTF{25_mai_colet_louise}

## Third Part

### Context

![context3](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/context3.png)

We have to find a discord invitation to the salon.

### Resolution

I struggled a lot with this one. I look on instagram, facebook, snapchat, linkedin, ...

I tried to find a google account, without success.

I found it on github. I searched for Louise Colet and found this:

![github_search](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/github_search.png)

At the bottom of the README.md, there is a link to the discord and the flag.

![flag3](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/flag3.png)

## Fourth Part

### Context

![context4](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/context4.png)

### Resolution

On discord, there is a channel "l-entrée"

![l_entree](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/l_entree.png)

After typing "le_petit_salon", we get access the the channel "le-petit-salon"

![petit-salon](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/petit-salon.png)

I typed the exact same text on google and found this website: https://fr.wikisource.org/wiki/Un_drame_dans_la_rue_de_Rivoli/1

![sol-petit-salon](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/sol-petit-salon.png)

It comes from a book from Louise Colet "Un drame dans la rue de Rivoli".
It was in 1835.

We get access to the channel "le-boudoire".

![le-boudoire](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/le-boudoire.png)

We have to complete this poem.

I just typed the verse we are given and found this site: https://www.persee.fr/doc/grif_0770-6081_1975_num_7_1_1458

![sol-le-boudoire](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/sol-le-boudoire.png)

We get access to the channel "le-fumoir".

![le-fumoir](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/le-fumoir.png)

We have to find where and when Louise Colet visited Victor Hugo for the first time.

I struggled a lot with that one. Finally, I found this book that talks about Louise Colet and Victor Hugo: https://gallica.bnf.fr/ark:/12148/bpt6k8572147#

![sol-le-fumoir](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/sol-le-fumoir.png)

Page 9, we learn that Louise Colet visited Victor Hugo for the first time in 1857 in Guernesey.

After validating this response, we get access to the channel "la-bibliothèque".

![flag4](/assets/img/CTFs/404CTF2023/osint/l_ame_d_un_poete_et_le_coeur_d_une_femme/flag4.png)

We have the flag 🥳 !!

I hope you enjoyed this writeup 😊 !
