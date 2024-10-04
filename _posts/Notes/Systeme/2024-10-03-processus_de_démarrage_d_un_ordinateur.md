---
title: 'AxelInsa.github.io | Notes | Processus de démarrage d'un ordinateur'
author: bipboup
date: 2024-10-03
categories: ['Notes', 'Systeme']
tags: ['Notes', 'Systeme']
permalink: /Notes/Systeme/boot_process
---

Le démarrage d'un ordinateur suit une série d'étapes essentielles qui permettent de passer du matériel allumé au système d'exploitation entièrement opérationnel. Ce processus est standardisé mais peut varier légèrement selon le type de firmware (BIOS ou UEFI) et le système d'exploitation utilisé (Windows, Linux, ou macOS).

![Linux startup process](/_posts/Notes/Systeme/img/power_on_diagram.png)


# 1. L'alimentation et le démarrage matériel

Le processus commence lorsque l'utilisateur allume l'ordinateur via le bouton d'alimentation. Le bloc d'alimentation convertit le courant alternatif en courant continu et fournit l'énergie nécessaire à tous les composants, notamment la carte mère, le processeur (CPU), la mémoire vive (RAM), et les périphériques de stockage.

# 2. Chargement du BIOS ou de l'UEFI

Le CPU, activé dès que l'alimentation est stable, recherche immédiatement un petit programme situé dans une mémoire ROM sur la carte mère : c’est le BIOS (Basic Input/Output System) ou l'UEFI (Unified Extensible Firmware Interface). Ce programme est responsable de charger les paramètres de configuration du système, qui sont modifiables via l’interface de configuration. Ces paramètres sont stockés sur une mémoire non volatile appelée CMOS(Complementary Metal-Oxide-Semiconductor) ou une mémoire flash sur la cartes mères modernes.

# 3. Test et initialisation du matériel : POST

Le BIOS ou l'UEFI exécute ensuite le POST (Power On Self Test), une série de tests qui vérifient que les composants matériels, tels que la RAM, le processeur, et les périphériques, fonctionnent correctement. Si une anomalie est détectée, l'ordinateur émet généralement un signal sonore d'alerte.

# 4. Recherche d'un périphérique de démarrage

Une fois le POST terminé avec succès, le BIOS ou l'UEFI recherche un périphérique de démarrage. Cela peut être un disque dur, un SSD, ou même un périphérique externe (comme une clé USB). Les utilisateurs peuvent configurer la séquence de démarrage dans les paramètres du BIOS ou de l'UEFI.

## 4.1. BIOS et MBR (Master Boot Record)

Dans les anciens systèmes utilisant le BIOS, le périphérique de démarrage doit contenir un MBR (Master Boot Record) sur les premiers secteurs du disque. Ce MBR (512 octets) contient un petit programme appelé "chargeur de démarrage" qui est chargé en mémoire et qui va commencer à démarrer le système d'exploitation.

## 4.2. UEFI et EFI System Partition (ESP)

Dans les systèmes plus récents, l'UEFI remplace le MBR cpar une partition système EFI (ESP), où sont stockés des fichiers exécutables pour démarrer le système d'exploitation. L'UEFI peut vérifier la signature de ces fichiers via le mécanisme de Seure Boot, afin de s'assurer que le système n'a pas été altéré.

L'UEFI lance le 

# 5. Chargement du chargeur de démarrage

Le BIOS ou l'UEFI trouve le programme de démarrage (bootloader) soit dans le MBR (BIOS) ou dans la partition EFI (UEFI). Le rôle du chargeur de démarrage est de charger le noyau du système d'exploitation en mémoire.

## 5.1. Windows : Bootmgfw.efi

Sur les systèmes Windows, avec UEFI, le fichier Bootmgfw.efi est chargé, qui à son tour cherche sur la partition "Windows boot" et exécute le chargeur de système d'exploitation winload.efi.

Si MBR est utilisé, le gestionnaire de démarrage bootmgr.exe est chargé depuis la partition système. Celui-ci cherche le chargeur de démarrage winload.exe dans /windows/system32 et l'exécute.  

Winload charge les pilotes matériels essentiels (marqués "BOOT_START") et lance le noyau Windows ntoskrnl.exe.

Une fois le noyau lancé, il démarre le processus de gestion des sessions (Smss.exe). Celui-ci démarre la session système et charge des pilotes supplémentaires.
Il démarre ensuite les services d'arrière-plan et prépare l'ordinateur pour l'utilisation (écran d'accueil, etc.).

## 5.2. Linux : GRUB

La plupart des distributions Linux utilisent GRUB (GRand Unified Bootloader). GRUB gère la gestion du chargement des systèmes d'exploitation sur le système.


![Linux startup process](/_posts/Notes/Systeme/img/Linux_startup_process_wip.png)

[Source de l'image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Linux_startup_process_wip.svg/578px-Linux_startup_process_wip.svg.png)


1. Initialisation

**Lecture de la configuration**: GRUB consulte son fichier de configuration principal (/boot/grub/grub.cfg) pour connaître les paramètres de démarrage.

2. Menu de démarrage

**Affichage du menu**:Si plusieurs noyaux ou systèmes d'exploitation sont disponibles, GRUB affiche un menu où l'utilisateur peut choisir celui à démarrer.

**Gestion des systèmes multiboot** : Si d'autres systèmes d'exploitation sont installés, GRUB peut les charger via un mécanisme de "chain loading", notamment pour des OS comme Windows​.

3. Chargement du noyau en mémoire

**Accès au noyau**:GRUB localise le noyau Linux dans le répertoire /boot (par exemple, vmlinuz-x.x.x) en utilisant ses capacités intégrées de lecture des systèmes de fichiers. 

**Chargement du noyau** : Une fois trouvé, le fichier du noyau est chargé en mémoire vive (RAM). GRUB transmet alors au noyau plusieurs paramètres initiaux nécessaires à son bon fonctionnement.

4. Transmission des paramètres initiaux

**initramfs (Initial RAM Filesystem)**: GRUB charge également le fichier initramfs (ou initrd), qui contient les pilotes et les modules nécessaires pour que le noyau puisse détecter le matériel et monter le système de fichiers racine plus tard.

**Système de fichiers racine**: GRUB spécifie la partition où se trouve le système de fichiers racine (ex : /dev/sda1) et transmet cette information au noyau via l'option root dans la configuration.

**Autres paramètres** : GRUB peut aussi transmettre des options comme ro (monter le système de fichiers en lecture seule) et quiet (réduire l'affichage des messages pendant le démarrage).

5. Transfert de contrôle au noyau

**Démarrage du noyau**: Après avoir chargé le noyau et les fichiers initramfs, GRUB transfère le contrôle complet au noyau Linux, qui poursuit l'initialisation du système.

**Montage du système de fichiers racine** : Le noyau utilise l'initramfs pour charger les pilotes nécessaires afin de détecter les périphériques de stockage et monter le véritable système de fichiers racine.


Le noyau démarre le système init. Celui-ci est systemd sur la plupart des distributions Linux modernes (init est configurable dans le fichier /etc/inittab). Celui-ci gère les services de démarrage et les autres processus utilisateur qui mènent à un invite de connexion. 


## 5.3. macOS : boot.efi

Sur un Mac, le fichier boot.efi est utilisé pour charger le noyau macOS, et le système continue de se charger de manière similaire à Windows ou Linux. (Section à compléter plus tard)

Conclusion

Le processus de démarrage d’un ordinateur est un enchaînement complexe mais bien structuré, reliant matériel et logiciel. Chaque étape est cruciale pour garantir que le système soit prêt à être utilisé. Que vous utilisiez Windows, Linux, ou macOS, les fondamentaux restent similaires, avec quelques différences notables en fonction du firmware et du type de système d'exploitation.

# Sources utilisées
- [Démarrage d'un PC sous Windows - Yannick Teach](https://www.youtube.com/watch?v=IPQ_sG4BOsE)
- [Que se passe-t-il exactement lorsque vous allumez votre ordinateur? - azurplus](https://azurplus.fr/que-se-passe-t-il-exactement-lorsque-vous-allumez-votre-ordinateur/)
- [Démarrage du système Linux - François Goffinet](https://linux.goffinet.org/administration/processus-et-demarrage/demarrage-du-systeme-linux/)
- [Démarrer (sous) LINUX - Jean-Luc Massat](https://jean-luc-massat.pedaweb.univ-amu.fr/ens/asr/cours-linux/demarrage-linux.html)
- [Processus de démarrage, Init et arrêt - RedHat](https://docs.redhat.com/fr/documentation/red_hat_enterprise_linux/5/html/installation_guide/ch-boot-init-shutdown)
- [Booting process of Linux - Wikipedia](https://en.wikipedia.org/wiki/Booting_process_of_Linux)
- [Étapes du démarrage d'un système Linux - developpez](https://linux.developpez.com/secubook/node15.php)
