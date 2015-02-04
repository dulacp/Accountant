# Accountant

> In the beginning God created man, and the costs followed afterwards.

This project is a concrete integration of the [django-accounting](https://github.com/dulaccc/django-accounting) application.
It is ready to be deployed on Heroku, but you can deploy on which provider you want.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/dulaccc/Accountant)


## Under the hood

- Python 3.3
- Django 1.7+
- [dj-static](https://github.com/kennethreitz/dj-static)
- Already configured for an Heroku deploy


## Manual deploy

```sh
$ heroku create accountant-x --region eu 
$ heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku addons:add mandrill:starter
$ heroku addons:add newrelic:wayne
$ heroku config:set DJANGO_SETTINGS_MODULE="accountant.settings.prod"
$ heroku config:set SECRET_KEY=`openssl rand -base64 32`
$ heroku config:set LOCAL_SERVER=0
$ heroku config:set SITE_MAIN_DOMAIN=accountant-x.herokuapp.com
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open
```

Then create your organization, add invoices, add bills, and enjoy !


## Local install

First create the virtualenv with the right python version

```sh
$ mkvirtualenv accountant --python=$(which python3)
$ workon accountant
```

Install the dependencies

```sh
$ pip install -r reqs/dev.txt
$ npm install
```

Create the local database

```sh
$ createdb accountant
$ ./manage.py migrate
```

Now run the server :

```sh
$ ./manage.py runserver
```


## Features

Maybe you want to integrate the accounting engine into your existing project, so check out [the features](https://github.com/dulaccc/django-accounting#features) offered by [django-accounting](https://github.com/dulaccc/django-accounting).


## Contact

[Pierre Dulac](http://github.com/dulaccc)  
[@dulaccc](https://twitter.com/dulaccc)

## License
Accounting is available under the MIT license. See the LICENSE file for more info.
