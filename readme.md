##  Install python3.8

## INSTALL AND RUN REDIS
### MAC OS : 
brew install redis 

### LINUX(DEBIAN/UBUNTU)

`sudo add-apt-repository ppa:redislabs/redis`

`sudo apt-get update`

`sudo apt-get install redis`


## SETTING UP VIRTUAL ENV FOR PYTHON

### INSTALL PACKAGE

`python3 -m pip install virtualenv`


### CREATE VIRTUAL ENV

`python3 -m virtualenv venv`

### ACTIVATE VIRTUAL ENV

`source venv/bin/activate`


## INSTALL DEPENDENCIES

`python3 -m pip install -r req-facedet.txt`


### CONFIGURING THE APP

`python3 manage.py collectstatic`

`python3 manage.py makemigrations`

`python3 manage.py migrate`


### RUN THE APP

`python3 manage.py runserver` 

