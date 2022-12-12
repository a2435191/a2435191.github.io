---
layout: post
title:  "DIY Google Analytics: Server-side data storage without a server"
date:   2022-12-10 05:19:00 -0600
categories: hackery
---
{% include hackery/page-views.html %}

<br>

I want to collect page views, but I'm cheap and don't want to pay for Google Analytics. So I rolled my own, using a [Google Form](https://forms.gle/T8Bq1EJabt3CJfYw7) to keep track of the page views, and any other metadata I might need.

```html
{% include hackery/page-views.html %}
```
<center><i>The source code for this page</i></center>

<br>

Cloudflare is used to get the current IP for determining unique visitors in the sheet. Then whenever I want to load the page views, I can download as a CSV a Google Sheets document [linked to the form](https://docs.google.com/spreadsheets/d/1xyH9pDgp9zkE0nVnggKAIhFUnvDhrg8l1XFMqd5MQF4/edit#gid=1433924867). For this example, I link to a public sheet that internally links to a private sheet using `=IMPORTRANGE`, so user IPs aren't exposed. In the private sheet, I have a Form Responses sheet and another sheet that uses `DCOUNTA` to get views and a `COUNTIF` `QUERY` Frankenstein formula to get unique views. One vulnerability I noticed and fixed (with `ARRAYFORMULA(TO_TEXT(...))`) stems from `QUERY` using the datatype of the *majority of the column*— if someone were to submit a bunch of numbers, comparisons could stop working as expected. 

{% include hackery/sliding-images.html %}
<br>

The downside for being cheap is that it's difficult and not at all secure. Please don't mess with it!

