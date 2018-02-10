# App Name
Potrait HAll

## Description
This is personal photo gallery where users can sign up and view all my favorie pictures as per per category. Users can also leave comments on the pictures
## User Stories
users can:
* View different photos that interest them.
* Click on a single photo to expand it and also view the details of the photo.
* Search for different categories of photos.
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Set Up and Installation

#### Prerequisites

* Python 3.6.2
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd watch
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE instagram ;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'potrait',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

* HTML5/CSS
* Bootstrap
* Python3.6
* Django Frane Work
* Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through khalifngeno@gmail.com or leave a comment here on github.

## License 

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Kipngetich Ngeno](https://github.com/Kipngetich33)

