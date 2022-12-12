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

Cloudflare is used to get the current IP for determining unique visitors in the sheet. Then whenever I want to load the page views, I can download as a CSV a Google Sheets document linked to the form.  (For this example, I link to a public sheet that internally links to a private sheet using `=IMPORTRANGE`, so user IPs aren't exposed.) The downside for being cheap is that it's difficult and not secure, of course. Please don't mess with it!