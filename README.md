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
`POST https://es-embassy.herokuapp.com/api/v1/accounts/login` 
`Parameters: username: arvind, password: 12345678`

## Singup
`POST https://es-embassy.herokuapp.com/api/v1/accounts/register` 
`Parameters:{
    "username": "", 
    "first_name": "", 
    "last_name": "", 
    "email": "", 
    "password": "", 
    "password_confirm": "" 
}`

## Get Profile
`GET https://es-embassy.herokuapp.com/api/v1/get_profile` 
`Header: Authorization: Token 2e9999174948645bde059a622f63abf030704d95`

## Get News
`GET https://es-embassy.herokuapp.com/api/v1/news` 
`Header: Authorization: Token 2e9999174948645bde059a622f63abf030704d95`

## API Paths
/api/login	esa_backend.views.login	
/api/sample_api	esa_backend.views.sample_api	
/api/v1/accounts/change-password/	rest_registration.api.views.change_password.change_password	rest_registration:change-password
/api/v1/accounts/login/	rest_registration.api.views.login.login	rest_registration:login
/api/v1/accounts/logout/	rest_registration.api.views.login.logout	rest_registration:logout
/api/v1/accounts/profile/	rest_registration.api.views.profile.profile	rest_registration:profile
/api/v1/accounts/register-email/	rest_registration.api.views.register_email.register_email	rest_registration:register-email
/api/v1/accounts/register/	rest_registration.api.views.register.register	rest_registration:register
/api/v1/accounts/reset-password/	rest_registration.api.views.reset_password.reset_password	rest_registration:reset-password
/api/v1/accounts/send-reset-password-link/	rest_registration.api.views.reset_password.send_reset_password_link	rest_registration:send-reset-password-link
/api/v1/accounts/verify-email/	rest_registration.api.views.register_email.verify_email	rest_registration:verify-email
/api/v1/accounts/verify-registration/	rest_registration.api.views.register.verify_registration	rest_registration:verify-registration
