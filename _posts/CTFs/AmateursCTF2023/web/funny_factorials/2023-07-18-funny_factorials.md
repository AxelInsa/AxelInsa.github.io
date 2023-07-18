---
title: 'CTFs | AmateursCTF2023 | Web | Funny Factorials'
author: Stillwolfing
date: 2023-07-18
categories: ['CTFs', 'AmateursCTF2023', 'Web']
tags: ['CTFs', 'AmateursCTF2023', 'Web']
permalink: /CTFs/AmateursCTF2023/web/funny_factorials
---

# Statement

![statement](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/statement.png)


# Website

Here is the main page.

![home](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/home.png)

We can calculate the factorial of a number (example 3).

![factorial](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/factorial.png)

We can change the theme of the page for cold or warm.

![theme](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/theme.png)

Note that the theme is a url parameter (themes/theme2.css) so maybe a LFI vulnerability is present.

# Application Source Code

For this challenge, we are given the source code of the app and the Dockerfile.

In the dockerfile, we can see that the flag is a root of the container.

![dockerfile](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/dockerfile.png)

Here is the function called when we make a GET request on the main page.

If the theme parameter is set, it opens it. Else, the theme themes/theme1.css is opened.

Then the index.html page is rendered using that theme.

![index](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/index.png)

We notice that the path to the theme is filtered by the function filter_path.

In the filter_path function, the "../" is removed. The thing is that it's done recursively so if the "....//" trick will not work. After one iteration it will become "../" and after another, it will disappear.

When the maximum amount of recursion is achieved, it triggers a Recursion error. If the path begins with "/", it is removed and the path is returned.

So, if we input the path //flag.txt, the first "/" is removed and the path "/flag.txt" is returned so the flag.txt file is used as a theme for the index.html page.

![filter_path](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/filter_path.png)

If we look at the \<style\> tag of the return page, we get the flag 🥳!

![flag](/assets/img/CTFs/AmateursCTF2023/web/funny_factorials/flag.png)

In this app, the lack of proper user input sanitization leads to a LFI vulnerability which allows us to recover the flag.

Another way to bypass the filter_path would be to put enough ../ to reach the Python default maximum recursion depth of 1000. I don't know if an url that long is allowed though. I did not try.









