##  Install python3.8

## INSTALL AND RUN REDIS
### MAC OS : 
`brew install redis `

### LINUX(DEBIAN/UBUNTU)

`sudo add-apt-repository ppa:redislabs/redis`

`sudo apt-get update`

`sudo apt-get install redis`

### CHECK INSTALLATION

Run this command

`redis-cli ping`

`PONG`

If pong is not returned, start the redis service using 

`redis-server`


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


## Notes:

1. Requires about 9mb RAM space per minuite of the session. So, session length is limited by available ram.
2. Emotion Recognition is based on only the image of the face. It's accuracy is reduced for accessories and facial hair. It may not be accurate if facial emotions are supressed and doesn't mirror what the person is feeling.
3. Face detection pipeline works on the server side and requires lot of processing power.

References:
1. [Deepface](https://sefiks.com/2021/03/02/deep-face-recognition-with-redis/)
2. [Face-Lib](https://justadudewhohacks.github.io/face-api.js/docs/index.html)
3. Django
4. Django Channels ASGI
5. Redis
