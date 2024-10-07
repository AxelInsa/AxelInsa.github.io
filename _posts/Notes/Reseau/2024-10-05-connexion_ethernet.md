---
title: Notes | Reseau | Connexion Ethernet
author: bipboup
date: 2024-10-05
categories: ['Notes', 'Systeme', 'Réseau']
tags: ['Notes', 'Systeme', 'Réseau']
permalink: /Notes/Reseau/connexion_ethernet
---

La connexion via un câble Ethernet déclenche une série de processus essentiels pour établir une communication réseau rapide et stable. De la détection du câble par la carte réseau à l'attribution d'une adresse IP, chaque étape implique une interaction entre le matériel et les protocoles réseau. Cet article détaille ces étapes pour les systèmes Linux et Windows, afin de comprendre comment les appareils réseau fonctionnent en pratique.

![Connexion Ethernet](/assets/img/Notes/Reseau/diagramme_connexion_ethernet.png)

# 1. Détection Physique du Câble Ethernet

Le processus de connexion Ethernet débute avec la détection physique du câble par la carte réseau (`NIC`).

**Interaction matérielle** : La carte réseau surveille l’état des broches de son port RJ45. Lorsqu’un câble est inséré, un **changement de tension** est détecté sur les broches, signalant la présence d’un autre appareil connecté (généralement un commutateur ou un routeur).

**Signaux de Link Pulse** : Une fois le câble détecté, la carte réseau envoie et reçoit des signaux appelés **link pulse**. Ces impulsions (`NLP` pour les réseaux de base et `FLP` pour les réseaux rapides) vérifient la continuité de la connexion. Ces signaux permettent de déterminer si le câble est correctement connecté à un appareil actif de l’autre côté.

**Interruptions matérielles (IRQ)** : Lorsque la carte réseau détecte un lien actif, elle génère une **interruption matérielle (IRQ)** pour notifier le système d’exploitation. Cette interruption est traitée par le pilote de la carte réseau, permettant au système de prendre en compte la nouvelle connexion réseau.

# 2. Autonegotiation : Négociation de la Vitesse et de la Duplexité

Après la détection du lien, la carte réseau et l’appareil connecté procèdent à une négociation des paramètres de connexion via le protocole d'autonégociation.

**Autonégociation (IEEE 802.3u)** : Ce protocole permet aux appareils de négocier automatiquement les meilleures conditions de communication, notamment la **vitesse** et le **mode de duplex**. Ils échangent des messages de **Link Pulse** pour déterminer leurs capacités respectives.

**Négociation de la vitesse** : Les cartes réseau modernes peuvent fonctionner à des vitesses variées (10 Mbps, 100 Mbps, 1 Gbps, etc.). Les deux appareils échangent leurs capacités et choisissent la vitesse la plus élevée supportée par les deux. Par exemple, si la carte réseau et le commutateur supportent 1 Gbps, ils établiront la connexion à cette vitesse.

**Mode Duplex** : La négociation détermine également si la connexion se fera en half-duplex (où un appareil envoie ou reçoit des données, mais pas les deux simultanément) ou en full-duplex (où les deux peuvent envoyer et recevoir en même temps). Le mode full-duplex est souvent préféré pour éviter les collisions et optimiser les performances.

# 3. Activation de l’Interface Réseau au Niveau du Système

## Sous Linux

Après le branchement d’un câble Ethernet, l’activation de l’interface réseau sous Linux est généralement automatisée, mais le processus peut varier selon la configuration du système et les outils utilisés pour la gestion réseau.

### Avec NetworkManager

La plupart des distributions Linux de bureau modernes utilisent NetworkManager pour gérer les interfaces réseau de manière automatique. Voici ce qui se passe lorsque le câble Ethernet est branché :

**Détection du lien** : NetworkManager détecte la présence d'un câble connecté à l'interface réseau (par exemple eth0 ou enp3s0). Cette détection repose sur les signaux de Link Pulse échangés entre la carte réseau et l'équipement de l'autre côté du câble (comme un commutateur).

**Activation automatique de l’interface** : Si l'interface est configurée pour démarrer automatiquement (ce qui est le cas par défaut), NetworkManager envoie une commande au noyau pour activer l’interface, l’équivalent de la commande :

```bash
ip link set dev eth0 up
```

À ce stade, l'interface est active et prête à envoyer et recevoir des paquets.

**Configuration IP via DHCP** : Après l'activation de l'interface, NetworkManager tente de récupérer une adresse IP via le protocole DHCP si l’interface est configurée pour cela. Cela implique l’envoi d’une requête DHCP Discover sur le réseau pour obtenir les informations nécessaires (adresse IP, passerelle par défaut, serveurs DNS).

Si un serveur DHCP est trouvé, l’adresse IP est automatiquement attribuée à l’interface, rendant la machine accessible sur le réseau local.

**Surveillance de l'état de la connexion** : NetworkManager continue de surveiller l’état de la connexion. Si le câble Ethernet est débranché, il désactivera automatiquement l’interface et cherchera une autre connexion disponible (comme le Wi-Fi).

### Utilisation de Systemd-networkd

Pour les systèmes sans NetworkManager, comme certains serveurs, systemd-networkd est souvent utilisé pour gérer les interfaces réseau :

**Configuration via fichiers .network** : Les interfaces réseau peuvent être configurées dans le répertoire `/etc/systemd/network/`. Un fichier typique pour une interface Ethernet utilisant DHCP pourrait ressembler à ceci :

```text
[Match]
Name=eth0

[Network]
DHCP=yes
```

Avec cette configuration, dès que le câble Ethernet est branché, systemd-networkd active automatiquement l’interface eth0 et envoie une requête DHCP pour obtenir une adresse IP.

**Activation automatique au démarrage** : Les interfaces configurées de cette manière sont activées au démarrage du système, et leur état est surveillé en permanence par systemd-networkd, qui gère les changements de connexion.

### Gestion manuelle avec ip et dhclient

Sur les systèmes minimalistes ou dépourvus de services de gestion de réseau comme NetworkManager ou systemd-networkd, l'activation de l'interface doit être effectuée manuellement :

**Activer l’interface** : Pour activer une interface nommée eth0, il faut utiliser la commande :

```bash
sudo ip link set dev eth0 up
```

Cela rend l'interface active, mais elle n’a pas encore d’adresse IP attribuée.

**Obtenir une adresse IP via DHCP** : Pour obtenir une adresse IP, il est possible d’utiliser le client DHCP dhclient :

```bash
sudo dhclient eth0
```

Cette commande envoie une requête DHCP Discover sur le réseau pour récupérer une adresse IP, une passerelle et des serveurs DNS, comme le ferait NetworkManager.

**Configuration IP statique** : Si une adresse IP statique est préférée, elle peut être attribuée manuellement avec :

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

Cette commande configure l'adresse IP 192.168.1.100 avec un masque de sous-réseau de 255.255.255.0 sur l’interface eth0.

Sur Linux, l'activation de l'interface réseau Ethernet après le branchement d’un câble est souvent gérée automatiquement par des services comme NetworkManager ou systemd-networkd. Ces outils simplifient la gestion réseau en configurant et surveillant les interfaces. Cependant, pour des configurations plus légères ou spécifiques aux serveurs, l’activation et la configuration peuvent être réalisées à la main, offrant ainsi un contrôle plus fin sur les paramètres réseau.

## Sous Windows

Après le branchement d'un câble Ethernet sur un système Windows, l'activation de l'interface réseau est largement automatisée. Windows dispose de plusieurs mécanismes pour gérer cette activation de manière transparente pour l'utilisateur, en utilisant des services intégrés et des pilotes compatibles.

### Automatisation via Plug-and-Play (PnP)

**Détection du périphérique** : Lorsque le câble Ethernet est connecté à la carte réseau, Windows détecte le changement de l'état du lien grâce à la fonctionnalité **Plug-and-Play** (`PnP`). Le système d’exploitation détecte l’activité sur le port Ethernet et identifie la carte réseau connectée.

**Chargement du pilote réseau** : Si le périphérique est correctement reconnu, Windows charge le pilote de la carte réseau. Ce pilote, souvent installé automatiquement lors de la première installation de la carte réseau, permet au système de communiquer avec le matériel réseau de manière standardisée.

### Configuration via NDIS (Network Driver Interface Specification)

Windows utilise le modèle `NDIS` pour gérer les interactions entre les pilotes de la carte réseau et le système d’exploitation :

**Interface standardisée** : NDIS fournit une interface standard entre le système d’exploitation et les pilotes de la carte réseau, ce qui permet à Windows de gérer des cartes de différents constructeurs de manière uniforme.

**Gestion des buffers et interruptions** : Le pilote, en coopération avec NDIS, configure les buffers en mémoire pour stocker les paquets réseau entrants et sortants et gère les interruptions matérielles (IRQ) pour notifier le système lorsque des paquets sont reçus ou lorsqu'un problème survient.

### Activation de l’interface réseau par les services Windows

Une fois la carte réseau détectée et le pilote chargé, Windows active automatiquement l'interface réseau :

**Service Network Connections** : Windows utilise le service Network Connections pour gérer les interfaces réseau. Ce service est responsable de l'activation des interfaces lorsqu’un lien est détecté, rendant l’interface prête à l'emploi sans intervention manuelle.

**Configuration IP via DHCP** : Par défaut, Windows configure les interfaces Ethernet pour obtenir une adresse IP de manière dynamique via DHCP. Lorsque le service Network Connections détecte que l’interface est active, il envoie une requête DHCP Discover pour obtenir une adresse IP, un masque de sous-réseau, une passerelle et les serveurs DNS.

Si un serveur DHCP est disponible sur le réseau, il répond avec une adresse IP et d'autres paramètres, que Windows applique automatiquement à l'interface. Cela permet à la machine de devenir immédiatement accessible sur le réseau.

**Surveillance de l’état de la connexion** : Windows continue de surveiller l’état de la connexion Ethernet via le Centre Réseau et Partage. Si le câble est débranché ou si la connexion échoue, l'interface est automatiquement désactivée et passe en mode "câble débranché".

### Activation manuelle de l'interface réseau

Bien que la plupart des processus soient automatisés, il est possible pour un utilisateur d’activer ou de désactiver manuellement une interface réseau à partir de l’interface graphique ou de la ligne de commande :

**Interface graphique** : L’utilisateur peut activer ou désactiver une interface réseau via le Panneau de configuration en accédant à :

```text
Panneau de configuration > Réseau et Internet > Connexions réseau
```

En cliquant avec le bouton droit sur l’interface Ethernet concernée, l’utilisateur peut choisir "Activer" ou "Désactiver" selon le besoin.

**PowerShell** : Pour les utilisateurs avancés, il est possible d’activer une interface réseau via PowerShell :

```powershell
Enable-NetAdapter -Name "Ethernet"
```

Cette commande active l’interface réseau nommée "Ethernet". L’interface devient alors disponible pour envoyer et recevoir des paquets, et si elle est configurée pour utiliser DHCP, elle tente immédiatement d'obtenir une adresse IP.

**Invite de commande** : La commande ipconfig /renew permet de forcer une requête DHCP pour obtenir une nouvelle adresse IP pour une interface active :

```powershell
ipconfig /renew
```

Cette commande est utile lorsque l’interface est déjà active mais a besoin de renouveler son bail DHCP ou si le serveur DHCP n'a pas répondu correctement lors de la première demande.

Sous Windows, l’activation de l'interface réseau après le branchement d'un câble Ethernet est conçue pour être transparente et automatisée. Grâce à des services comme Plug-and-Play et Network Connections, le système d'exploitation gère l'activation, la configuration et la surveillance des interfaces réseau sans nécessiter d’intervention manuelle. Cependant, les options de configuration via PowerShell et l’interface graphique permettent de garder un contrôle manuel pour les utilisateurs avancés ou dans des situations de dépannage.

# 4. Attribution d’une Adresse IP via DHCP

Si la machine n’a pas d’adresse IP statique préconfigurée, elle utilise le protocole **DHCP** (Dynamic Host Configuration Protocol) pour obtenir une adresse IP de manière dynamique.

**Découverte DHCP (DHCP Discover)** : La machine envoie un message DHCP Discover en **broadcast** pour trouver un serveur DHCP sur le réseau. Ce message est diffusé à l'adresse IP spéciale 255.255.255.255 pour s'assurer qu'il est reçu par tous les appareils du réseau, et en particulier par le serveur DHCP.

**Offre DHCP (DHCP Offer)** : Le serveur DHCP répond avec un message DHCP Offer, qui propose une adresse IP, un masque de sous-réseau, une passerelle par défaut, et les serveurs DNS.

**Demande DHCP (DHCP Request)** : La machine répond à cette offre en envoyant un message DHCP Request en **broadcast**, confirmant qu’elle accepte l’adresse IP proposée. Ce processus empêche d’autres serveurs DHCP sur le réseau de tenter d’attribuer la même adresse IP à un autre appareil.

**Accusé de réception DHCP (DHCP Ack)** : Le serveur DHCP finalise le processus en envoyant un message DHCP Ack, confirmant la réservation de l’adresse IP pour une durée déterminée (le bail DHCP). La machine configure alors son adresse IP et les autres paramètres réseau reçus.

# 5. Envoi des Trames ARP pour Découvrir le Réseau

Après l’activation de l’interface, la machine doit identifier les autres appareils sur le réseau local, et c’est ici qu’intervient le protocole ARP (Address Resolution Protocol).

**Fonctionnement de l’ARP** : Chaque appareil sur un réseau local possède une adresse MAC (Media Access Control), une adresse physique unique attribuée à sa carte réseau. Pour envoyer des données à un appareil sur le même réseau, la machine doit connaître l’adresse MAC associée à l’adresse IP cible.

**Requête ARP** : La machine envoie une trame ARP en broadcast à tous les appareils du réseau local : "Qui a l’adresse IP X ?". Cela signifie qu’elle cherche l’adresse MAC de l’appareil ayant l’adresse IP X. Cette trame est envoyée à l’adresse MAC spéciale ff:ff:ff:ff:ff:ff, qui signifie que tous les appareils sur le réseau doivent la traiter.

**Réponse ARP** : L’appareil qui possède l’adresse IP X répond en envoyant une trame ARP en unicast, directement à l’expéditeur, contenant son adresse MAC. Ainsi, la machine émettrice peut associer l’adresse IP à l’adresse MAC dans son cache ARP.

**Cache ARP** : Pour éviter de refaire une requête ARP à chaque fois qu’elle souhaite communiquer avec la même adresse IP, la machine stocke cette correspondance dans un **cache ARP**. Ce cache a une durée de vie limitée, et les entrées expirent après un certain temps, ce qui permet de garder les informations à jour.

# Conclusion

Brancher un câble Ethernet déclenche une chaîne d'événements impliquant des interactions entre matériel, logiciels systèmes et protocoles réseau. Chaque étape contribue à l’établissement d’une connexion réseau stable et performante. Comprendre ces mécanismes en profondeur est crucial pour toute personne travaillant dans l'administration système et réseau, car cela permet de diagnostiquer des problèmes et d’optimiser les connexions réseau.
