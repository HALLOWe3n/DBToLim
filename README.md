# DBToLim

[![CircleCI](https://circleci.com/gh/HALLOWe3n/DBToLim.svg?style=svg)](https://circleci.com/gh/HALLOWe3n/DBToLim)
[![GitHub license](https://img.shields.io/github/license/HALLOWe3n/DBToLim)](https://github.com/HALLOWe3n/DBToLim/blob/master/LICENSE)

## Technical task for get offer
Simple API application

# Tech
### Stack:
- Python 3.7.5
- Django 2.2.6
- PostgreSQL 11

### Infrastructure
- CircleCI (Auto Deploy)
- Heroku

### Installation

create virtual environment

 - if you use linux input this command in terminal: 
```bash
sudo apt-get install python3-venv
```

```python3
python3 -m venv venv
```

activate venv
```bash
source venv/bin/activate
```

Create a database in PostgreSQL
in the env.sh file there is information about which database, user and password should be

##### next
Activate bash script to export environment variables to the virtual environment
```bash
. env.sh
```

Migrate data to database 
```python3
python manage.py migrate
```

Create superuser for admin
```python3
python manage.py createsuperuser
```

Collectstatic
```python3
python manage.py collectstatic
```

> and

Run server
```python3
python manage.py runserver
```

Documentation API be on the way
(http://localhost:8000/docs/) --> swagger


## Application deployed on Heroku
### Also uses CircleCI for auto deployment and tests.

(https://dbtolimit.herokuapp.com/)
the start page will return the code 400 - do not worry :)
go to (https://dbtolimit.herokuapp.com/docs/)
there will also be documentation

To enter the admin panel:
- admin
- Pass12345

# Enjoy
