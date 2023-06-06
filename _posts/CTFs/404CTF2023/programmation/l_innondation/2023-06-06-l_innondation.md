---
title: CTFs | 404CTF2023 | Programmation | L'innondation
author: Stillwolfing
date: 2023-06-06
categories: ['CTFs', '404CTF2023', 'Programmation']
tags: ['CTFs', '404CTF2023', 'Programmation']
permalink: /CTFs/404CTF2023/Programmation/l_innondation
---

Here is the context:

![context](/assets/img/CTFs/404CTF2023/programmation/l_innondation/context.png)

The challenge asks us to count rhinoceros. Let's connect via netcat to understand what it is about.

Here is what we get when we connect:

![nc](/assets/img/CTFs/404CTF2023/programmation/l_innondation/nc.png)

We have to count the number of rhinoceros ~c`°^) in the text and send the answer within seconds.

The fact is that it will ask us to do it several times so we have to make an infinite while loop to count each wave of rhinoceros.

Here is the code I wrote:
```python
import pwn
import re

# connect to the server
r = pwn.remote('challenges.404ctf.fr', 31420)

iter = 0

while True:
    print("Iteration: " + str(iter))
    iter += 1
    try:
        # receive the response
        response = r.recvuntil(b'>')
        print(response.decode())

        # count the number of ~c`°^) in the response
        count = len(re.findall(r'~c`°\^\)', response.decode()))
        print("Count: " + str(count))

        # send the count
        r.sendline(bytes(str(count), 'utf-8'))
    except:
        break

# receive the flag
response = r.recvuntil(b'}')
print(response.decode())
```

For each loop iteration, we receive until the character '>' so we know we have the full response. Then we count the number of rhinoceros using regex. We send the count.

When we reach the end, the character '>' will not be in the response. It will raise an error because it takes too much time. When it happens, we know it's done so we break out of the loop.

We receive until the character '}' (the end of the flag) and print the response.

![flag](/assets/img/CTFs/404CTF2023/programmation/l_innondation/flag.png)

We have the flag !

I hope this writeup was easy to understand. Have a good day 😀 !





