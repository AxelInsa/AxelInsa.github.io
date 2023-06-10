---
title: CTFs | 404CTF2023 | Hardware |  Un réveil difficile
author: Stillwolfing
date: 2023-06-10
categories: ['CTFs', '404CTF2023', 'Hardware']
tags: ['CTFs', '404CTF2023', 'Hardware']
permalink: /CTFs/404CTF2023/hardware/un_reveil_difficile
---

## Context

![context](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/context.png)

We are given the "reveil.circ" file.

## Resolution

Looking at the net, CIRC is a file extension commonly associated with Logisim Circuit files. This kind of file is used by "Logisim" software.

We download the software (I chose the java version to not have problems on my VM) and we run it.

```sh
java -jar logisim-generic-2.7.1.jar &
```

We open the "reveil.circ" file (File > Open)

![main](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/main.png)

The assignement tells us to display "Un_c" on the output.

To do this, we can modify bits in the input and see how it affects the output.

Playing a bit with, I understood that the row i represents the i-th output.

Each bit switch on and off one segment in the output.

So, we can just try to switch on and off until we get the result we want (since each bit in the input affect only one segment, we don't have to resolve equations).

![un_c](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/un_c.png)

Changing the output like this, we get "Un_c". From what I understood, we just have to spam the clock and it will reveal us the flag.

If a character is ambiguous, we choose first the number then the uppercase and then the lowercase.

The flag format is 404CTF{le_message_que_vous_avez_trouvé}

### First Round

404CTF{Un_c

## Second Round

![2_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/2_round.png)

404CTF{Un_cH1FF

## Third Round

![3_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/3_round.png)

404CTF{Un_cH1FFrA9e

## Fourth Round

![4_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/4_round.png)

404CTF{Un_cH1FFrA9e_A55

## Fifth Round

![5_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/5_round.png)

404CTF{Un_cH1FFrA9e_A55e2_b

## Sixth Round

![6_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/6_round.png)

404CTF{Un_cH1FFrA9e_A55e2_bi3n_

## Seventh Round

![7_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/7_round.png)

404CTF{Un_cH1FFrA9e_A55e2_bi3n_d3Pr

## Last Round

![last_round](/assets/img/CTFs/404CTF2023/hardware/un_reveil_difficile/last_round.png)

404CTF{Un_cH1FFrA9e_A55e2_bi3n_d3PreCie}

We obtained the flag !
