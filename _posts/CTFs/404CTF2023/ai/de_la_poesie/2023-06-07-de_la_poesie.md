---
title: CTFs | 404CTF2023 | Ai | De la poésie
author: Stillwolfing
date: 2023-06-07
categories: ['CTFs', '404CTF2023', 'Ai']
tags: ['CTFs', '404CTF2023', 'Ai']
permalink: /CTFs/404CTF2023/ai/de_la_poesie
---

Here is the context:

![context](/assets/img/CTFs/404CTF2023/ai/de_la_poesie/context.png)

We are given the file "poeme.zip". Inside of it, there are images of hand written numbers:

![poeme](/assets/img/CTFs/404CTF2023/ai/de_la_poesie/poeme.png)

It is the dataset MNIST, a known dataset in deep learning.

I found this colab online that trains a CNN on this dataset: [MNIST](https://colab.research.google.com/github/skorch-dev/skorch/blob/master/notebooks/MNIST.ipynb)

I put the poeme.zip file on my drive and added this code at the end of the colab:

```python
from google.colab import drive
drive.mount('/content/drive')

!cp drive/MyDrive/poeme.zip .
!unzip poeme.zip

import os
from PIL import Image
from torchvision.transforms import ToTensor
predictions = []
work_dir = os.getcwd() 
for i in range(6536):
  img_path = os.path.join(work_dir, 'images', str(i) + '.jpg')
  img = Image.open(img_path).convert('L')
  img = ToTensor()(img)
  img = img.unsqueeze(0)
  pred_result = cnn.predict(img)
  predictions.append(str(pred_result[0]))

print(''.join(predictions))
```

I trained the AI and got the predictions for the numbers.

I put the result in a txt file named "code.txt".

The name of the book where the "poeme" is from is called "Être pair ou ne pas l'être" (to be even or not to be).

I thought maybe we have to replace each number in the sequence by 1 if the number is odd and 0 if the number is even to form bits.

```python
with open("code.txt", "r") as f:
    data = f.read()

bits = []
for char in data:
    if int(char) % 2 == 0:
        bits += "0"
    else:
        bits += "1"
print(bits)
```

There are 6536 images which is a multiple of 8. So I can form bytes by grouping them by 8 bits.

```python
# create groups of 8 characters
groups = [bits[i:i+8] for i in range(0, len(bits), 8)]
groups = ["".join(group) for group in groups]
print(groups)
```

Then I can try to form ascii characters by considering that the numbers obtained are ascii codes.

```python
# convert to ascii
ascii_values = [int(group, 2) for group in groups]
print(ascii_values)

# get the characters
ascii_values = [chr(group) for group in ascii_values]
print(ascii_values)

# convert to string
string = "".join(ascii_values)
print(string)
```

We kind of retrieved the poeme:

```txt
Et2e pair ou ne paS lettre

Lâhomme, dont la vie entiÃ¨re
Est de 96 ans,
Dort le 1/3 de sa carriÃ¨re,
Ã'est juste 32 ans.Ajoutons pour ma|adies,
Procès, voyages, accidents
Au moins 1/4 de la vie

C'ast0encore 2 foi3 12 ans.
Par!jour 2 heuRes d'études
Ou de travaux - foNt 8 ans,
Noirs chagrins, inquiétudes
Pour le double vont 16 ans.Pour affaires qu'on projette
1/2-heure, - encobe 2 aîs.
5/4 d'heures de toilette
Barbe et caetera - 7 ans.J
Par jour pour manger et boire
2 font bien 8 ans.
Cela porte le mémoire
Jusqu'à 95 ans.Rdste encorm 1 an pour faire
Ce qu'oiseaux font au printemps.
Par jour l'homme a donc sur terre
1/4 d'heure de bon temps.
Juste assez pour déposE2 le drapeau sur le 424CTF : 
404CTF{d#_L4_p03S1e_qU3lqU3_P;u_C0nT3mp0r4in3}
oème original : Le quast d'heure de bon temps Nicolas Boileau$
```

There are a lot of errors. The AI did not well recognized some numbers so we do not get the good ascii character.

The flag is understable, we can guess which letters are not good.

Final flag: 404CTF{d3_L4_p03S1e_qU3lqU3_P3u_C0nT3mp0r4in3}

I hope you enjoyed this writeup. If you want to know more about CNNs, there are a lot of great articles out there. Take your time to read it.



















