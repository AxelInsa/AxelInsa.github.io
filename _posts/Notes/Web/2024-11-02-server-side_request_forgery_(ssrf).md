---
title: Notes | Server-Side Request Forgery (SSRF)
author: bipboup
date: 2024-11-02
categories: ['Notes', 'Web'] 
tags: ['Notes', 'Web'] 
permalink: /Notes/Web/server-side_request_forgery_(ssrf)
---


# Qu'est-ce qu'une vulnérabilité **SSRF** (Server-Side Request Forgery) ?

La **SSRF** est une vulnérabilité qui permet à un attaquant de manipuler un serveur pour qu'il effectue des requêtes vers des ressources externes ou internes non prévues.
En utilisant une **SSRF**, un attaquant peut contourner les **firewallls**, les **ACLs** (Access Control List) et les **IPS** (Intrusion Prevention System) et accéder à des services internes protégés.

Dans une SSRF classique, un attaquant exploite une application web vulnérable pour forcer le serveur à accéder à des systèmes internes comme des bases de données, des services d'authentification ou des interfaces de gestion.


# Impact potentiel d'une SSRF

Une attaque SSRF réussie peut permettre:
- **L'accès à des données sensibles** (fichiers de configuration, métadonnées d'instances cloud, etc.).
- La **cartographie** et le **balayage des ports réseaux** pour identifier des services ouverts.
- La **compromission des services internes** en exploitant des vulnérabilités supplémentaires.
- Dans certains cas, une **exécution de code** (RCE) sur le système distant.


# Types d'attaques SSRF

Les attaques SSRF peuvent cibler soit le serveur lui-même, soit d'autres services internes.

## 1. SSRF contre le serveur local

L'attaquant manipule le serveur pour qu'il se connecte à lui-même en utilisant l'interface de *loopback* (`localhost` ou `127.0.0.1`). Cela peut permettre d'accéder à des interfaces d'administration ou de gestion qui ne sont accessibles que depuis le réseau interne.

Exemple: Un attaquant peut forcer le serveur à accéder à `https://localhost/admin` pour contourner les contrôles d'accès et accéder aux fonctionnalités d'administration. Il peut également forcer le serveur à accéder à `https://localhost:8080/manager/html` pour accéder à des interfaces de gestion qui est un service interne accessible uniquement depuis le réseau interne.

> Il est possible de récupérer l'adresse **IPv6** du serveur en utilisant une SSRF. Par exemple, sur HTB, il n’y a généralement pas de véritable résolution DNS publique pour les machines, à moins que l'on ne soit sur des environnements spécifiques comme les *Active Directory labs* ou des challenges particuliers. Ainsi, impossible d'utiliser `dig` pour obtenir l'adresse IPv6 du serveur.
Si vous découvrez une SSRF ou une méthode permettant au site web de faire des requêtes, vous pouvez envoyer une requête vers votre propre serveur en utilisant l'IPv6 de votre serveur. Cela vous permet d'obtenir l'adresse IPv6 du serveur cible. Si le pare-feu filtre les requêtes IPv6 différemment, il est parfois possible d'accéder à des services qui ne sont pas protégés de la même manière qu'en IPv4. 
{: .prompt-info}

## 2. SSRF contre des services internes

Un attaquant peut également manipuler le serveur pour accéder à des systèmes non exposés publiquement mais accessibles par le serveur.

Exemple: Accéder à `http://192.168.0.15/admin` pour exploiter un service interne.

## 3. SSRF aveugle

Dans certains cas, l'attaquant ne voit pas directement la réponse de la requête envoyée, mais peut en déduire le succès via des indices indirects tels que des **retards de réponse** ou des **erreurs d'accès**.


# Techniques de contournement des protections SSRF

Les applications tentent souvent de limiter les attaques SSRF par l'utilisation de liste **noire** ou **blanche**. Cependant les attaquants peuvent contourner ces protections grâce à diverses techniques.

- Utilisation d'**alternatives de l'adresse IP**: `127.0.0.1` peut être écrite `2130706433` en décimal, `017700000001` en octal, `::1` en IPv6, etc.
- **Encodage d'URL**: Des caractères comme `@`, `#` ou `//` peuvent être utilisés pour tromper la validation de l'URL.
- Exploitation des **redirections ouvertes**: Profiter d'une redirection non sécurisée pour se rediriger vers la cible réelle.
- Utilisation de **schéma d'URL inhabituel**: Les schémats comme `file://` ou `dict://` peuvent donner accès à des fichiers locaux ou d'autres services réseau.


# Points d'entrée d'une SSRF

Les points d'entrée d'une SSRF sont souvent facile à trouver car beaucoup des requêtes contiennent URLs entiers. D'autres points d'entrée sont plus difficiles à identifier.

## URLs partielles

Parfois, une application peut prendre un *hostname* ou une partie de l'URL comme entrée. Celle ci est incorporé dans une URL complète au niveau backend.

Exemple, dans une application qui prend un nom de domaine comme entrée, l'utilisateur peut entrer un nom de domaine partiel comme `www.example.com` ou `example.com`. Cette partie est alors intégrée dans l'URL de la requête, comme `https://www.example.com/admin`.

Cette exemple est simple mais parfois l'exploitation peut être limité car on ne contrôle par tout l'URL.

## URL dans les formats de données

Certaines applications peuvent transmettre des URL dans des formats de données tels que **JSON** ou **XML**.

Par exemple, si une application accepte des données en format **XML** et les *parses*, celle-ci peut être vulnérable aux injections **XXE** (*XML External Entity*). Cette application pourrait aussi être vulnérable aux SSRF via l'exploitation de la **XXE**.

## `Referer` header

Certaines application utilisent le header `Referer` à des fins de tracking et de statistiques. Certains site visitent le site précisé dans le referer pour analyser le contenu de la page, le type de balise utilisée, etc. Ainsi l'en-tête `Referer` peut être utilisé comme un point d'entrée pour une SSRF dans ce type de cas assez spécifique.

# Exemples de scénarios

- **Balayage de ports internes** : L’attaquant cartographie les ports ouverts sur des serveurs internes en envoyant des requêtes et en mesurant le temps de réponse.

- **Accès aux métadonnées des services cloud** : Sur AWS, les métadonnées de l’instance sont accessibles via http://169.254.169.254/. L’attaquant peut extraire des informations sensibles, comme des informations d'authentification.

- **Exécution de commandes à distance** : En utilisant des SSRF pour accéder à des services sans authentification comme Redis ou Memcached, un attaquant peut mener des attaques RCE (Remote Code Execution).


# Prévenir les attaques SSRF

Pour prévenir les attaques SSRF, il est nécessaire d'appliquer plusieurs couches de sécurité:

## Contrôle réseau

- **Segmenter le réseau**: Limite l'accès aux ressources critiques.
- **Règles de pare-feu strictes**: Appliquer des règles "deny-all" pour limiter l'accès aux réseaux internes.

## Contrôle applicative

- **Validation stricte des entrées**: Vérifiez et nettoyer toutes les entrées utilisateur.
- **Listes blanches d'URL**: On n'utilise pas de liste noire. Autoriser uniquement les domaines ou IP spécifiques absolument nécessaires.
- **Désactiver les schémas d'URL inutiles**: Restreindre les schémas aux seuls schémas nécessaires (ex: `http`, `https`).
- **Filtrage des réponses**: Ne pas renvoyer les réponses brutes au client. Filtrer les réponses pour ne renvoyer que les données nécessaires.

## Protéger les services internes

- **Authentification des services**: Protéger les services critiques par authentification même sur des réseaux internes.
- **Limiter les permissions**: Appliquer le principe du moindre privilège pour limiter l'accès aux services internes.

## Surveillance et détection

Utiliser des outils de détection pour identifier les vulnérabilités SSRF et les attaques qui peuvent les exploiter.


# Conclusion

Les vulnérabilités SSRF représentent une menace sérieuse pour architectures modernes. En 2021, celle-ci apparaît comme une catégorie à part entière dans le **TOP 10** des vulnérabilités des applications web de l'**OWASP**. L'essor des environnements cloud et des API favorisent la présence de ces attaques. Bien qu'il soit difficile de les prévenir complètment, une défense en profondeur combinant une segementation réseau, une validation strictes des entrées et une configuration adéquates des services internes peut réduire les risques.


# Sources

- https://portswigger.net/web-security/ssrf
- https://owasp.org/Top10/fr/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/
- https://www.vaadata.com/blog/fr/comprendre-la-vulnerabilite-web-server-side-request-forgery-1/
- https://www.cyberuniversity.com/post/ssrf-server-side-request-forgery-quest-ce-que-cest
- https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/
- https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf
- https://cheatsheetseries.owasp.org/assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf
- https://owasp.org/Top10/fr/
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Request%20Forgery/README.md