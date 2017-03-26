# Legal Checkup

## Description
(to be added)

## Team Members
- Siddharth Kumar (Project Manager)
- Stephanie Shi (Technical Lead)
- Suzanne Knop
- Brandon Obas

## Setting up

##### Clone the repo

```
$ git clone https://github.com/hack4impact/legal-checkup.git
$ cd legal-checkup
```

##### Initialize a virtualenv

```
$ pip install virtualenv
$ virtualenv -p /path/to/python3.x/installation env
$ source env/bin/activate
```

For mac users it will most likely be
```
$ pip install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```
Note: if you are using a python2.x version, point the -p value towards your python2.x path

##### (If you're on a mac) Make sure xcode tools are installed

```
$ xcode-select --install
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Other dependencies for running locally

You need to [Redis](http://redis.io/), and [Sass](http://sass-lang.com/). Chances are, these commands will work:

**Sass:**

```
$ gem install sass
```

**Redis:**

_Mac (using [homebrew](http://brew.sh/)):_

```
$ brew install redis
```

_Linux:_

```
$ sudo apt-get install redis-server
```

You will also need to install **PostgresQL**

_Mac (using homebrew):_

```
brew install postgresql
```

_Linux (based on this [issue](https://github.com/hack4impact/flask-base/issues/96)):_

```
sudo apt-get install libpq-dev
```

##### Create the database

```
$ python manage.py recreate_db
```

##### Other setup (e.g. creating roles in database)

```
$ python manage.py setup_dev
```

##### [Optional] Add fake data to the database

```
$ python manage.py add_fake_data
```

## Running the app

```
$ source env/bin/activate
$ honcho start -f Local
```
