---
title: CTFs | 404CTF2023 | Crypto | Dessine-moi une courbe elliptique
author: Stillwolfing
date: 2023-06-08
categories: ['CTFs', '404CTF2023', 'Crypto']
tags: ['CTFs', '404CTF2023', 'Crypto', 'Elliptic Curve']
permalink: /CTFs/404CTF2023/crypto/dessine_moi_une_courbe_elliptique
---

## Context

![context1](/assets/img/CTFs/404CTF2023/crypto/dessine-moi_une_courbe_elliptique/context1.png)
![context2](/assets/img/CTFs/404CTF2023/crypto/dessine-moi_une_courbe_elliptique/context2.png)

We are given the code used to crypt the flag and some other informations.

## Code

Here is the code given:

```python
from sage.all import EllipticCurve, GF
import hashlib
from Crypto.Cipher import AES
from secret import FLAG
from os import urandom

p = 231933770389389338159753408142515592951889415487365399671635245679612352781
a = ?
b = ?

determinant = 4 * a**3 + 27 * b**2
assert determinant != 0

E = EllipticCurve(GF(p), [a,b])
G = E.random_point()
H = E.random_point()

print(G.xy()[0], G.xy()[1])
print(H.xy()[0], H.xy()[1])
print(p)

iv = urandom(16)
key = str(a) + str(b)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
cipher = aes.encrypt(FLAG)
print(cipher.hex())
print(iv.hex())
```

The flag is crypted using AES. The key used in the encryption is key = str(a) + str(b).

So, in order to find the key, we need to find a et b.

## Resolution

a and b are the coefficients of an elliptic curve defined over a finite field. They determine the shape and properties of the curve.

The code asserts that the determinant of the curve, calculated using ```determinant = 4 * a**3 + 27 * b**2```, is not zero. This check ensures that the curve is non-singular and can be used for cryptographic operations.

After defining the elliptic curve E using the coefficients a and b, the code generates two random points G and H on the curve.

In the code p is the prime modulus of the finite field over which the curve is defined.

We know that sage uses the Weierstrass equation for the elliptic curve.

So, we have:

```
G_y ** 2 = G_x ** 3 + a * G_x + b
H_y ** 2 = H_x ** 3 + a * H_x + b
```

By isolating b,

```
G_y ** 2 - G_x ** 3 - a * G_x = H_y ** 2 - H_x ** 3 - a * H_x
```

```
a * G_x - a * H_x = G_y ** 2 - G_x ** 3 - H_y ** 2 + H_x ** 3
```

```
a * (G_x - H_x) = (G_y ** 2 - G_x ** 3) - (H_y ** 2 - H_x ** 3)
```

So, we have
```
a = (G_y ** 2 - G_x ** 3) - (H_y ** 2 - H_x ** 3) / (G_x - H_x)

b = G_y ** 2 - G_x ** 3 - a * G_x
```

## Implementation

I defined a function to ensure the results of each operations are modulo p:

```python
def moins(x, y, p):
    return (x % p - y % p + p) % p
```

We calculate a and b:

```python
# Solve for a
a = moins(moins(G_y ** 2, H_y ** 2, p), moins(G_x ** 3, H_x ** 3, p), p) * pow(moins(G_x, H_x, p), -1, p) % p

# Solve for b using one of the expressions for b
b = moins(G_y ** 2, G_x ** 3, p)
b = moins(b, a * G_x % p, p)
```

We can now decrypt the flag:

```python
key = str(a) + str(b)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
flag = aes.decrypt(secret_message)

print(flag.decode())
```

Output:

![flag](/assets/img/CTFs/404CTF2023/crypto/dessine-moi_une_courbe_elliptique/flag.png)
