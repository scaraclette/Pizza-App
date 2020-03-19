# Pizza App

## Video Demo: https://youtu.be/C-pXDM8F9qQ
Transforming <a href="http://www.pinocchiospizza.net/">Pinocchio's Pizza & Subs</a> static website into a Django web application. New web application will let users order and pay online. Project includes authentication, cart, admin capabilities.<br>
Based on Harvard's CS50web's Project 3: https://docs.cs50.net/web/2020/x/projects/3/project3.html

![Imgur](https://i.imgur.com/neaOkba.png)

# To start application locally
```
$ pip3 install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
# Other notes
Personal touch: this project has an added Stripe API for payment method. 
