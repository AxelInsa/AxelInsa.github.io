---
title: CTFs | 404CTF2023 | Steganography | Les Félicitations
author: Stillwolfing
date: 2023-06-09
categories: ['CTFs', '404CTF2023', 'Steganography']
tags: ['CTFs', '404CTF2023', 'Steganography']
permalink: /CTFs/404CTF2023/steganography/les_felicitations
---

## Context

![context](/assets/img/CTFs/404CTF2023/steganography/les_felicitations/context.png)

We are given a text and we have to find congratulations in it.

Here is the text:

```txt
Tous étaient réunis dans la salle,
Criblant leur feuille de mots et posant leurs esprits sur papier.
Très encouragés par le déroulement des opérations,
Il suffisait simplement de les regarder pour voir leur dévotion
.-.. . -.-. --- -.. . -- --- .-. ... . -.-. . ... - ... -.-- -- .--. .-
Beaucoup d'entre eux étaient fiers de leur oeuvre
Cillant à peine quand dehors, un monstre jappait
Fierté mène cependant à orgueil
Et n'oubliez pas qu'orgueil mène à perte.
-- .- .. ... .-.. .- -.-. .- ... . .-. - .- .-. .. . -. .... .- .... .-
Juste au moment où leurs travaux allaient finir,
Hors du laboratoire, un cri retentissant fut émis
Peu d'humains avaient entendu ce genre de cris.
Exténués par cette énième attaque, les scientifiques se remirent au travail.
```

The morse code is useless, it's just a delimiter.

I struggled a lot on this challenge. My first idea was pick a word in each paragraph in order to create a sentence of 3 words. After a lot of research, it ends up with nothing.

Then I found in the first paragraph that if I pick the 1st letter of the 1st line, the 2nd letter of the 2nd line, the 3rd letter of the 3rd line, the 4th line of the 4th line, I get the "Très".

By doing the same thing of the other 2 paragraphs, I get the words "Bien" and "Joué".

Congratulations sentence: "Très Bien Joué".

The flag is: 404CTF{TrèsBienJoué}

