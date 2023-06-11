---
title: CTFs | 404CTF2023 | Osint | Les OSINTables [1/3]
author: Stillwolfing
date: 2023-06-11
categories: ['CTFs', '404CTF2023', 'Osint']
tags: ['CTFs', '404CTF2023', 'Osint']
permalink: /CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D
---

This challenge is in 3 parts. I only solved the first one.

## First Part

### Context

![context](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/context.png)

We are given this photo:

![photo](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/photo.jpg)

We have to find Cosette's address

### Resolution

Thanks to the photo, we know that her street is "Rue Victor Hugo" and that her city begins with "VE".

Also at the bottom right of the letter, we can see the number "04". I think it's a phone number.

![france_phone_number_map](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/france_phone_number_map.png)

Looking at the France's phone number map, we know that Cosette lives in the south east of France.

On the left of the letter, there is a roman digit: LXXXIII -> 83.

I don't know why it's written in roman but it may be the house number.

![maps_search](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/maps_search.png)

Searching for "83 rue Victor Hugo" on google maps, there is one city that begins with "Ve": Vergèze.

![france_phone_number_map](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/maps_vergeze.png)

Vergèze is in the south east, it could be there.

By taking a guess at the flag, we found it: 404CTF{83_rue_victor_hugo_vergeze}

I took a look at the second part of the challenge and can show you what I found.

## Second Part

### Context

![context2](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/context2.png)

This time, we have to find Jean Valjean address.

We knows that:
-  He lives in Paris
-  He is in one of the buildings with the most floors near his metro station.
- He dislikes alcohol drinkers.
- He likes to be close to his money.

His email address is "jean.valjean750075@gmail.com".

## Resolution

We know that he lives in Paris so we can reduce the research to Paris.

He is in one of the buildings with the most floors near his metro station -> If we can find the station, we can probably find the building.

He dislikes alcohol drinkers -> He might lives near a bar or a night club.

He likes to be close to his money. -> He lives in a wealthy neighborhood or near banks (don't know the meaning of the sentence).

Thanks to his email address and [Epios](https://epieos.com/), we found out that his calendar is public.

![calendar](/assets/img/CTFs/404CTF2023/osint/les_osintables_%5B1_on_3%5D/calendar.png)

For each event, he wrote the time it takes for his go there (by foot or from his station or both combined).

He know that:
- the "Conservatoire National Supérieur de Musique et de Danse de Paris" is at 21 minutes of travel time (probably by foot).
- the "Musée du Quai Branly" is at 28 minutes using transports.
- "Jardin du Luxembourg" is at 25 minutes from his station (probably by foot).
- Victor's house is at 32 minutes (don't know the transport).
- The cinema "Les 7 Batignolles" is at 18 minutes (metro + walk)

I did not search further but it's good leads.

I hope you enjoyed this writeup 🙂 !
