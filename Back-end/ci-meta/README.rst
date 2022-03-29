Ci - meta
--------------------------------------------------------------

- Install dependencies ::

    # Download & install python 3.8.8 at https://www.python.org/downloads/
    # flask
    $ pip3 install Flask
    # flask sqlalchemy
    $ pip3 install flask-sqlalchemy
    $ pip install -U flask-cors

- The app requires a Postgres database whose credentials must be updated into config.py

- Run it::


    $ export FLASK_APP=app
    # Create an admin user
    $ flask fab create-admin
    # Run dev server
    $ flask run

That's it!!
