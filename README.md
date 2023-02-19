# Star Wars Explorer

## Codebase setup
    $ git clone https://github.com/IvanKansazov/adverity-challenge
    $ cd adverity-challenge
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

## Database setup
    $ mysql -u db_user -p
    CREATE DATABASE db_name;\q
#### Create db.cnf file from template
    $ cd adverity && cp db.cnf.example db.cnf
    
#### Enter database credentials
    $ vi db.cnf 
#### Migrations
    $ cd ../
    $ python manage.py migrate

## Start 
    $ python manage.py runserver
