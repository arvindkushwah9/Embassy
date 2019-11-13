# esa_backend

Getting the local dev server running first time
# Install Python 3.6.8
pip 19.3.1 

pipenv install 
pipenv shell 
./manage.py makemigrations 
./manage.py migrate 
./manage.py runserver 
If dependencies already installed 
pipenv shell 
./manage.py runserver

## OR

sudo pip install -r requirements.txt 
pip install djangorestframework 
python3 manage.py makemigrations 
python3 manage.py migrate 
python3 manage.py runserver 
If dependencies already installed 
python3 manage.py runserver 

#API

## Login
`POST http://127.0.0.1:8000/api/login` 
`Parameters: username: arvind, password: 12345678`

## Simple api
`POST http://127.0.0.1:8000/api/sample_api` 
`Header: Authorization: Token 2e9999174948645bde059a622f63abf030704d95`