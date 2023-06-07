---
title: CTFs | 404CTF2023 | Web3 | L'Antiquaire, tête en l'air
author: Stillwolfing
date: 2023-06-07
categories: ['CTFs', '404CTF2023', 'Web3']
tags: ['CTFs', '404CTF2023', 'Web3']
permalink: /CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air
---

## Context

![context](/assets/img/CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air/context.png)

We have to find the password of this person.

We have the memorandum.txt file.

This file is a Memo. A Memo is a short message or description that is attached to a transaction or interaction on a blockchain network.

When you perform a transaction on a blockchain network, such as sending cryptocurrency tokens from one address to another, you may have the option to include a memo. The memo is an optional field where you can include additional information about the transaction.


## Resolution

The memo is in hexadecimal, we need to decode it.

```python
import binascii

with open('memorandum.txt', 'r') as f:
    memo = f.read()

memo_bytes = binascii.unhexlify(memo)
print(memo_bytes)
```

At the end of the decoded text, there is:

![end_decoded](/assets/img/CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air/end_decoded.png)

We have this URL: https://shorturl.ac/mysecretpassword that is a Rick Roll.

We this other kind of endpoint:

```
/ipfs/bafybeia5g2umnaq5x5bt5drt2jodpsvfiauv5mowjv6mu7q5tmqufmo47i/metadata.json
```

By searching the net, I learned that IPFS (InterPlanetary File System) is a peer-to-peer distributed file system designed to create a more decentralized and resilient web infrastructure. It is a protocol that enables the storage and retrieval of files on a global scale without relying on traditional centralized servers.

Thanks to this site, we know how to use it: https://decrypt.co/resources/how-to-use-ipfs-the-backbone-of-web3

I searched for it on ipfs.io:

```
https://ipfs.io/ipfs/bafybeia5g2umnaq5x5bt5drt2jodpsvfiauv5mowjv6mu7q5tmqufmo47i/metadata.json
```

We end up on this JSON file:

![metadata.json](/assets/img/CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air/metadata.json.png)

Another file is mentionned (ipfs://bafybeic6ea7qi5ctdp6s6msddd7hwuic3boumwknrirlakftr2yrgnfiga/mystere.png).

We access the file the same way.

![mystere](/assets/img/CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air/mystere.png)

It looks like a token for an account. I found on the net that Sepolia is a blockchain.

I searched for the account we have on https://sepolia.etherscan.io/

![profile](/assets/img/CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air/profile.png)

In the "Contracts" tab, in the Constructor Arguments, there is the flag !!

![flag](/assets/img/CTFs/404CTF2023/web3/l_antiquaire_tete_en_l_air/flag.png)
