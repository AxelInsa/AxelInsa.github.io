
# FCSC 2023: Tri Selectif
## Stillwolfing

Here is the context:

![context](/assets/img/CTFs/FCSC2023/Intro/tri_selectif/context.png)


We are given the source code of the application and a base code to connect to the application and interact:

App:

```python
import os

def usage():
	print('Actions possibles:')
	print('  - "comparer X Y": compare les valeurs du tableau aux cases X et Y, et retourne 1 si la valeur en X est inférieure ou égale à celle en Y, 0 sinon.')
	print('  - "echanger X Y": échange les valeurs du tableau aux cases X et Y, et affiche le taleau modifié.')
	print('  - "longueur:      retourne la longueur du tableau.')
	print('  - "verifier:      retourne le flag si le tableau est trié.')

def printArray(A):
	print(" ".join("*" for a in A))

def verifier(A):
	return all([ A[i] <= A[i + 1] for i in range(len(A) - 1) ])

if __name__ == "__main__":

	A = list(os.urandom(32))
	print("Votre but est de trier un tableau dont vous ne voyez pas les valeurs (chacune est remplacée par *) :")
	printArray(A)
	usage()
	B = A[:]

	try:
		while True:
			x = input(">>> ")

			if x.startswith("comparer"):
				x, y = list(map(int, x.split(" ")[1:]))
				print(int(A[x] <= A[y]))
			
			elif x.startswith("echanger"):
				x, y = list(map(int, x.split(" ")[1:]))
				A[x], A[y] = A[y], A[x]

			elif x.startswith("longueur"):
				print(len(A))

			elif x.startswith("verifier"):
				c = verifier(A)
				if c:
					flag = open("flag.txt").read().strip()
					print(f"Le flag est : {flag}")
				else:
					print("Erreur : le tableau n'est pas trié")
					print(f"Le tableau de départ était : {B}")
					print(f"Le tableau final est :       {A}")
				print("Bye bye!")
				break

			else:
				usage()
	except:
		print("Erreur : vérifier les commandes envoyées.")
```

Client:

```python
#!/usr/bin/env python3

# python3 -m pip install pwntools
from pwn import *

# Paramètres de connexion
HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2051

def comparer(x, y):
	io.sendlineafter(b">>> ", f"comparer {x} {y}".encode())
	return int(io.recvline().strip().decode())

def echanger(x, y):
	io.sendlineafter(b">>> ", f"echanger {x} {y}".encode())

def longueur():
	io.sendlineafter(b">>> ", b"longueur")
	return int(io.recvline().strip().decode())

def verifier():
	io.sendlineafter(b">>> ", b"verifier")
	r = io.recvline().strip().decode()
	if "flag" in r:
		print(r)
	else:
		print(io.recvline().strip().decode())
		print(io.recvline().strip().decode())

def trier(N):
	#############################
	#   ... Complétez ici ...   #
	# Ajoutez votre code Python #
	#############################
	if comparer(0, 1):
		echanger(0, 1)
	pass

# Ouvre la connexion au serveur
io = remote(HOST, PORT)

# Récupère la longueur du tableau
N = longueur()

# Appel de la fonction de tri que vous devez écrire
trier(N)

# Verification
verifier()

# Fermeture de la connexion
io.close()
```

We have to implement the "trier" function. The challenge is pretty easy, we can implement the most basic sort algorithm like this:

```python
def trier(N):
	#############################
	#   ... Complétez ici ...   #
	# Ajoutez votre code Python #
	#############################

	i = 0
	while i < N - 1:
		j = i + 1
		while j < N:
			if not comparer(i, j):
				echanger(i, j)
			j += 1
		i += 1
```

Then we run the client:

```python
python client_sol.py
```

![flag](/assets/img/CTFs/FCSC2023/Intro/tri_selectif/flag.png)

We have the flag, nice!