---
layout: page
title: Install
nav_order: 2
description: "How to install Tafferugli."
permalink: /install/
---

# Getting started

Tafferugli is a web application based on django.

Following, we report installation instructions for [Ubuntu/Debian systems](#requirements) and [docker](#docker). If you need help installing it on an other system, [ask!](/contact)


## Requirements 


Install python3 and pip

```bash
apt install python3
apt install python3-pip
```

Install [graph-tool](https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions) libraries, necessary to do some analysis on community graphs.

```bash
# Change DISTRIBUTION to match yours
echo "deb [ arch=amd64 ] http://downloads.skewed.de/apt DISTRIBUTION main" >> /etc/apt/sources.list
apt-key adv --keyserver keys.openpgp.org --recv-key 612DEFB798507F25
apt update
apt install python3-graph-tool python3-cairo
```
(Remember to change DISTRIBUTION with yours. It can be one of: bullseye, buster, sid, bionic, disco, eoan). You can find out by issuing the command ```lsb_release -cs```.


## Installation


```bash
git clone https://github.com/sowdust/tafferugli.git
cd tafferugli
virtualenv --system-site-packages -p python3 env
. env/bin/activate
pip install -r requirements.txt
```


## Configuration

You can configure some entries in the file settings.py. Also, remember to **change the default value of SECRET_KEY** with any random string of that length (50 characters - no whitespaces).

By default, Tafferugli is configured to run locally and to use a SQLite database. However, SQLite does not manage concurrency very well, often returning the error "Database is locked". 
For this reason and for performance, it is strongly recommended to setup and use another database backend (PostgreSQL or MySQL). The file settings.py already contains a default database configuration for PostgreSQL.


## Set up the application


```bash
python manage.py makemigrations
python manage.py makemigrations twitter
python manage.py migrate
python manage.py createsuperuser
# Follow the instructions to create one admin user
```


## Run the application


To run the application locally on your machine:

```bash
python manage.py runserver
```

On a different terminal, execute the background tasks that run the streamers and the metrics computation:


```bash
python manage.py process_tasks
```

If you want to have more control on the background processes, you can execute them in three different terminals (maybe in a ```screen``` session):

```bash
python manage.py process_tasks --queue streamers-queue
python manage.py process_tasks --queue operations
python manage.py process_tasks --queue metrics-computation

```

See [django-background-tasks.readthedocs.io](https://django-background-tasks.readthedocs.io/) for more information.


## Upgrade

The application is currently being developed, with bugs fixed and features introduced quite often.
If you want to upgrade to the latest version, navigate to the root folder, pull the most recent updates from github and upgrade the database schema in case it was modified:

```bash
git pull
python manage.py makemigrations twitter
python manage.py migrate
```


## Docker 

People from [lab61](https://www.lab61.org/) have provided the following "all-in-one" docker file.
It is only for development purposes and it is not intended to be run in production. 


```docker
FROM tiagopeixoto/graph-tool:latest
RUN yes | pacman -S python-cairo
RUN yes | pacman -S python-pip
RUN yes | pacman -S git
RUN yes | pacman -S sqlite
RUN pip install virtualenv
RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/sowdust/tafferugli.git
WORKDIR tafferugli
RUN virtualenv --system-site-packages -p python3 env
RUN source env/bin/activate
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py makemigrations twitter
RUN python manage.py migrate
# creating user with admin pass credentials
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
# creating a file to startup the application
RUN echo "#!/bin/bash" > startup.sh
RUN echo "/usr/bin/python manage.py process_tasks &" >> startup.sh
RUN echo "/usr/bin/python manage.py runserver 0.0.0.0:8000" >> startup.sh
# run the created .sh file
RUN chmod +x startup.sh
EXPOSE 8000
CMD ./startup.sh
```


