Install virtualenv-
-------------------------

    pip install virtualenv
    virtualenv eztest
    source eztest/bin/activate
    
Clone Project:
-------------------------

    git clone https://github.com/dadasoz/eztest.git
    cd eztest

Install requirements:
-------------------------

    pip install -r requirements.txt


Run Migrations:
-------------------------

    python manage.py makemigrations
    python manage.py migrate

Run server:
-------------------------

    python manage.py runserver


Default Username and Passwords:
-------------------------

    admin   Test@321
    dadaso  Test@321
    nishant Test@321
    vishal  Test@321


Features:
-------------------------

    Login
    Registration
    Chat - Realtime using websockets

API's-
-------------------------

    http://127.0.0.1:8000/api/chat/get-users/
    
    http://127.0.0.1:8000/api/chat/get-messages/?receiver=1
    
    http://127.0.0.1:8000/api/chat/get-messages/?receiver=1&sender=2 --> Not sefe as per security

