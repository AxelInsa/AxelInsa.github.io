---
title: CTFs | FCSC2023 | Web | Enisa Flag Store 1
author: Stillwolfing
date: 2023-05-06
categories: [CTFs, FCSC2023, Web]
tags: [CTF, FCSC, Web, SQLI]
permalink: /CTFs/FCSC2023/web/enisa_flag_store_1
---

Here is the context:

![context](/assets/img/CTFs/FCSC2023/web/enisa_flag_store_1/context.png)

I did not solved this challenge during the CTF, but I solved it after.

We are given the source code of the website

It's a pretty simple website, we can register, login, logout, and see the flag of our team.

To register, we need to provide a username, a password, a token and a team name. The form request looks like this:

![form](/assets/img/CTFs/FCSC2023/web/enisa_flag_store_1/form.png)

I provided the token given in the challenge description.

When I connect, I'm given an auth cookie and end up on the main page.

![main_connected](/assets/img/CTFs/FCSC2023/web/enisa_flag_store_1/main_connected.png)

And can show the flag of my team.

![flag_page](/assets/img/CTFs/FCSC2023/web/enisa_flag_store_1/flag_page.png)

First I thought I had to crack the auth cookie, but it was a dead end.

Then looking at the source code, I noticed that all the queries were prepared except one:

![query](/assets/img/CTFs/FCSC2023/web/enisa_flag_store_1/query.png)

This query is in the getData function, which is called when we want to see the flag of our team.

Since the query is not prepared, we can perform a SQL injection.

When we register, we can provide a team name, which is not sanitized. So, I registered with the following team name:

```
username=sqli&password=sqli&token=ohnah7bairahPh5oon7naqu1caib8euh&country=fr'+or+1%3d1--+-
```

The country is: fr' or 1=1-- -

So, when we want to see the flag of our team, the query will be:

```sql
SELECT ctf, challenge, flag, points FROM flags WHERE country = 'fr' or 1=1-- -
```

It will display all the flags.

![flag](/assets/img/CTFs/FCSC2023/web/enisa_flag_store_1/flag.png)

We've got the flag !

It's a simple sqli but I struggled to do it during the CTF, I was stuck on the auth cookie. Besides the code is 600 lines long and it's easy to miss something.

I hope you enjoyed this writeup, see you next time !
