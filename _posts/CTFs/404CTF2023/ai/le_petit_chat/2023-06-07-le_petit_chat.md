---
title: CTFs | 404CTF2023 | Ai | Le Petit Chat
author: Stillwolfing
date: 2023-06-07
categories: ['CTFs', '404CTF2023', 'Ai']
tags: ['CTFs', '404CTF2023', 'Ai']
permalink: /CTFs/404CTF2023/ai/le_petit_chat
---


## Context

```txt
Ebloui par les reflets du soleil sur l'imposante vitrine du café littéraire lors d'une éclaircie, vous plissez les yeux et marquez un temps d'arrêt. Une boule dorée attire votre attention. Tiens, ce n'est pas une boule, mais un petit chat orange, le regard absorbé par la vitrine luisante. Vous vous étonnez de remarquer des lunettes de soleil surplombant ses magnifiques moustaches blanches, il semble étrangement équipé en cette pluvieuse journée. Par curisosité, vous sortez du café et vous vous approchez discrètement, ayant senti votre mouvement, le chat se retourna.

« Vous ne seriez pas Hackademicien par hasard, dit-il, d'un air effrayé.

— Non pourquoi ?

Soulagé, le petit chat se retourna complètement, se leva de tout son long sur ses deux pattes arrières, frotta ses griffes sur son pelage et vous tendit la patte.

— Je suis le Chat botté ! Ravi de faire votre connaissance !

N'étant pas plus surpris de voir un chat qui parle qu'un chat avec des lunettes languissant devant un café littéraire, vous décidez de tendre votre main à votre tour.

— Mon maître, Monsieur le Marquis de Carabas m'attend dans ce café, malheureusement, je ne peux pas le rejoindre, les chiens sont interdits.

— Et alors ? Vous êtes un chat, vous devriez pouvoir entrer.

— Justement, je suis censé pouvoir rentrer, mais l'intelligence artificielle qui garde l'entrée se mélange les neurones ! Voilà qu'elle confond les chiens et les chats.

— C'est très dérangeant.

— À cause de ce dysfonctionnement, je me retrouve dehors, dit-il, en levant ses lunettes et en vous regardant intensément avec ses gros yeux noirs et son aura envoûtante.

— Vous allez m'aider, n'est-ce pas ?

Ne sachant que répondre face à cette claire injustice, vous décidez seulement d'acquiescer de la tête. Satisfait, le chat s'approcha et vous proposa à voix basse :

— Vous vous y connaissez dans l'art du camouflage ? Oui ? Excellent, c'est exactement ce qu'il me faut. J'ai entendu dire que le thé était très apprécié dans cet endroit, pouvez-vous m'aider à me faire passer pour une théière ? Cela me permettrait de rejoindre mon maître ! »

Ne pouvant plus faire demi-tour, vous prenez une profonde respiration pour vous concentrer sur votre objectif : transformer ce petit chat roux en théière !

Pour valider le challenge, il faudra upload votre image de chat modifié sur internet et récupérer son URL. Enfin, il vous suffira de vous connecter via netcat et d'entrer l'URL du chat modifié. Voici un site possible : https://imgtr.ee/. L'image originale est téléchargeable ci-dessous : chat.jpg.

Vous pouvez vous aider du script verificateur.py afin d'avoir le modèle utilisé et de pouvoir essayer en local. Attention ! Ne ~modifiez~~ pas trop le petit chat, il faut que son maître puisse le reconnaître.

Un peu de lecture pour trouver l'inspiration : http://clpav.fr/lecture-chat-botte.htm. (Ne sert à rien pour résoudre le challenge)
```

We have been provided with an image of a cat and the code utilized by the server to verify whether the AI predicts a teapot and ensure that the image hasn't been excessively altered.


## Code

Here is the code:

```python
# Python 3.11.3
import numpy as np
import tensorflow as tf
from urllib import request
from PIL import Image
from TresTresSecret import drapeau


def main(file):
    je_merite_le_drapeau = True
    chat_modifie = Image.open(file)

    # Modèle utilisé : ResNet50 de TensorFlow
    model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')

    # Mise du chat dans le réseau
    image_raw = tf.io.read_file(file)
    image = tf.image.decode_image(image_raw)

    # Prétraitement de l'image : on utilise directement la fonction de ResNet50
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = image[None, ...]

    # Prédiction de l'image
    image_probs = model.predict(image)
    _, image_class, class_confidence = tf.keras.applications.resnet50.decode_predictions(image_probs, top=1)[0][0]

    # On vérifie que c'est bien une théière
    if image_class != 'teapot':
        je_merite_le_drapeau = False

    # On cherche le vrai chat
    chat = Image.open('chat.jpg')
    taille = chat.size

    # On utilise la norme L2
    def distance(a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    # On vérifie enfin si le chat n'a pas été trop ~modifié~~
    eps = 70
    for x in range(taille[0]):
        for y in range(taille[1]):
            if distance(chat.getpixel((x, y)), chat_modifie.getpixel((x, y))) > eps:
                je_merite_le_drapeau = False

    if je_merite_le_drapeau:
        print(f'Je mérite le drapeau. Le voici : {drapeau}')
    else:
        print('Je ne mérite pas le drapeau')


try:
    url = input('URL du chat > ')
    file = request.urlretrieve(url)[0]
    main(file)
except Exception as e:
    print(f'Je n\'ai pas récupéré ton chat ! {str(e)}')

```

The code asks the user to enter the image URL and retrieve the image from the url provided.

Then it makes a prediction for the image using the ai. If the image is predicted as teapot, it verifies that we did not modifie the image too much.

The code iterates over each pixel of the image and calculate the distance between the 2 colors. To do this, each (r, g, b) value is considered as a vector. It calculates the difference between the pixel vector of the original cat and the pixel vector of the modified cat. Then it calculates the norm of the resulting vector. The L2 norm is used in this case, which means that the coordinates are squared, summed, and then the square root is taken to obtain the final length.

If the length of this resulting norm is superior to 70, we modified too much.

So, we have to make small changes to each pixel in order to make the AI predict the image is a teapot.

## Adversarial Attacks

After some research, I stumbled upon this colab: [Adversarial Attacks](https://colab.research.google.com/github/phlippe/uvadlc_notebooks/blob/master/docs/tutorial_notebooks/tutorial10/Adversarial_Attacks.ipynb#scrollTo=CaFRbmOWTlDO)

This colab / article explains what is an Adversarial Attack and how to do it.

Adversarial attacks are techniques used to manipulate the behavior of machine learning models by making imperceptible changes to input data. These changes are carefully crafted to deceive the model into producing incorrect or unintended outputs. Adversarial attacks exploit vulnerabilities in the way machine learning models generalize from training data.

In the colab, they perform a Fast Gradient Sign Method (FGSM), an untargeted attack, which means that they try to increase the ground truth error in order for the model to predict any other class.

Then they perform a Patch Adversarial attack. The patch adversarial attack is a type of adversarial attack where a small, specifically crafted patch is added to an image to deceive a machine learning model. The patch is designed to cause misclassification or induce a desired behavior in the model when it encounters images with the patch.

In our case, we cannot use this type of targeted attack because it would modify too much the pixel values.

In the untargeted attack they perform, they compute the gradient and modify the image pixels in order to increase the loss. It is the inverse of the gradient descent.

Objective:

- Gradient Descent: The objective of gradient descent is to minimize a loss function by iteratively adjusting the model parameters in the direction of steepest descent.

- Adversarial Attacks: The objective of adversarial attacks is to manipulate the behavior of a machine learning model by generating input examples that induce misclassification or desired behaviors.

Direction of Optimization:

- Gradient Descent: It optimizes the model parameters in the direction of decreasing loss by computing gradients with respect to the model parameters.

- Adversarial Attacks: It optimizes the input examples in the direction that maximizes the model's loss or causes a specific behavior, typically by computing gradients with respect to the input.

Goal:

- Gradient Descent: The goal of gradient descent is to find the optimal set of model parameters that minimize the loss on the training data and improve the model's generalization.

- Adversarial Attacks: The goal of adversarial attacks is to exploit vulnerabilities in the model's decision-making process, potentially causing misclassification or influencing the model's behavior.

Optimization Process:

- Gradient Descent: It typically involves computing gradients of the loss function with respect to the model parameters and updating the parameters in the opposite direction of the gradients. This process is repeated iteratively until convergence.

- Adversarial Attacks: It often uses optimization techniques, such as gradient-based methods, to find perturbations that maximize the loss or influence the model's behavior. The optimization process iteratively adjusts the perturbations until the desired effect is achieved.

Inputs and Outputs:

- Gradient Descent: It takes input features and corresponding labels as input and aims to optimize the model's parameters to predict the correct labels.

- Adversarial Attacks: It takes input examples and aims to modify them in a way that causes misclassification or induces specific behaviors from the model.


The first attack presented in the article can still be used. Here they increase the loss of the ground truth class. We can perform a targeted attack by choosing a class and making changes to pixels in order to reduce the loss for this class.

After digging the net, I stumbled upon this github that is truly fantastic: [Targeted Adversarial Attacks](https://github.com/aaronchong888/Targeted-Adversarial-Attacks)

We just download the repo, install the requirements and run this command:

```sh
python generate_adversarial_example_targeted.py <input_file_name> <target_class_name>
```

We input the cat image given and select the teapot class.

The program will perform 300 iterations. Each iteration calculate the loss for the teapot class, calculate the gradient and make the right changes to the pixel values in order to reduce the loss associated with the teapot class.

After the 300 iterations, it saves the image obtained.

Here is the original image:

![chat](/assets/img/CTFs/404CTF2023/ai/le_petit_chat/chat.jpg)

Here is the modified image:

![chat_modifie](/assets/img/CTFs/404CTF2023/ai/le_petit_chat/chat_modifie.png)

The model predicts a teapot with a confidence of 99.9%.

I uploaded the image online (https://www.noelshack.com/) and send the url to server via netcat.

![flag](/assets/img/CTFs/404CTF2023/ai/le_petit_chat/flag.png)

We've got the flag. I hope you learned a lot in this writeup. I discovered something I had no idea it existed thanks to this challenge.
