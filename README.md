# Accountant

> In the beginning God created man, and the costs followed afterwards.

This project is a concrete integration of the [django-accounting](https://github.com/dulaccc/django-accounting) application.
It is ready to be deployed on Heroku, but you can deploy on which provider you want.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


## Under the hood

- Python 3.3
- Django 1.7+
- [dj-static](https://github.com/kennethreitz/dj-static)
- Already configured for an Heroku deploy


## Features

Maybe you want to integrate the accounting engine into your existing project, so check out [the features](https://github.com/dulaccc/django-accounting#features) offered by [django-accounting](https://github.com/dulaccc/django-accounting).


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


## Deploy the beast

### Prepare the static server

#### create a new user

```sh
$ aws iam create-user --user-name heroku-accountant
```

**output**
```json
{
    "User": {
        "UserName": "heroku-accountant",
        "Path": "/",
        "CreateDate": "2015-01-22T14:10:08.058Z",
        "UserId": "<user_id>",
        "Arn": "arn:aws:iam::<user_arn_id>:user/heroku-accountant"
    }
}
```

#### give the user some access keys

```sh
$ aws iam create-access-key --user-name heroku-accountant
```

**output**
```json
{
    "AccessKey": {
        "UserName": "heroku-accountant",
        "Status": "Active",
        "CreateDate": "2015-01-22T14:18:56.237Z",
        "SecretAccessKey": "<secret_key>",
        "AccessKeyId": "<access_key>"
    }
}
```

Write down the `<secret_key>` and `<access_key>` values, so that we can give the values to the heroku app.

#### create the aws bucket

```sh
$ aws s3 mb s3://accountantx --region eu-west-1
```

#### give the user access to the created bucket

```sh
$ aws iam put-user-policy --user-name heroku-accountant --policy-name AmazonS3FullAccess-heroku-accountant --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": "arn:aws:s3:::accountantx",
            "Condition": {}
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
                "s3:DeleteObjectVersion",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:GetObjectVersion",
                "s3:GetObjectVersionAcl",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectAclVersion"
            ],
            "Resource": "arn:aws:s3:::accountantx/*",
            "Condition": {}
        }
    ]
}'
```


### Deploy the app

> We need to specify the buildpack to use otherwise heroku won't know which one to choose, due to the fact that both `package.json` and `requirements.txt` files exist.

Lancer les commandes dans l'ordre ci-dessous:

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
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set AWS_STORAGE_BUCKET_NAME=accountantx AWS_S3_ACCESS_KEY_ID="<access_key>" AWS_S3_SECRET_ACCESS_KEY="<secret_key>"
$ git push heroku master
$ ./manage.py collectstatic --noinput
$ aws s3 sync --acl public-read accountant/static s3://accountantx/static/
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open
```

And you're done !


## Cheatsheet

I've defined some shortcuts in the `Makefile`, feel free to explore those or add yours.

_**d**eploy to **p**roduction_
```sh
$ make dp
```

_**d**eploy & **m**igrate to **p**roduction_
```sh
$ make dmp
```

_**c**ollectstatic to **p**roduction_
```sh
$ make cp
```


## Contact

[Pierre Dulac](http://github.com/dulaccc)  
[@dulaccc](https://twitter.com/dulaccc)

## License
Accounting is available under the MIT license. See the LICENSE file for more info.
