datahack / visualizer
=====================
 
It shows the infant mortality rates in India, in a certain year (probably it was 2005) ( data obtained from http://data.gov.in/ ) spread across the states, through a heatmap.

> This was a quick prototype, developed within really constrained time limits. 
> I don't remember the exact source of the data. 

It was a product of [a day-long hackthon (journalists + coders)](https://www.facebook.com/media/set/?set=oa.476488175739797&type=1), that [took place around Feb'13](http://satyaakam.net/?p=746). This repo is a revised version of the same, compatible with Django 1.6.* 

***

![Infant Mortality Rate Sample](https://raw.githubusercontent.com/arcolife/datahack/master/static/img/datahack.png)


**Usage**

(requires Django 1.6)

> python manage.py runserver

Go to http://localhost:8000 to browse India's position on the map, 
zoom right in to see the distribution.

**Major credits:**

* @bhanuvrat
* @kanteshraj
* @ramniquesingh
* @satyaakam
