# miniwallet

first clone this repository  to a new directory

     git clone https://github.com/sabith9567/miniwallet.git

create virtual environment ,
for osx users

     virtualenv -p python3

activate and install requirements.txt

    pip install -r requirement.txt

also run

    python manage.py migrate

load dump form dbfinal.json / create super user and add one/two users and note down the id from backend
     
     python manage.py loaddata dbfinal.json

if loaded from dumb you can use token corresponding to user

      bb80ff23-2e84-42db-95bd-ca7f6985c57a	admin
      0fa07a26-4c83-47a7-ae0a-4dabc68b728a	testuser2

you can import the https://www.getpostman.com/collections/8b5cb731d04111a2e618 post man collection and look to the apis and test it

there is also an ui for adding amount , with an unique UUID as reference id from 
http://localhost:8000/frontend/add-to-wallet/
