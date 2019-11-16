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




/accounts/login/	django.contrib.auth.views.LoginView	login
/accounts/logout/	django.contrib.auth.views.LogoutView	logout
/accounts/password_change/	django.contrib.auth.views.PasswordChangeView	password_change
/accounts/password_change/done/	django.contrib.auth.views.PasswordChangeDoneView	password_change_done
/accounts/password_reset/	django.contrib.auth.views.PasswordResetView	password_reset
/accounts/password_reset/done/	django.contrib.auth.views.PasswordResetDoneView	password_reset_done
/accounts/reset/<uidb64>/<token>/	django.contrib.auth.views.PasswordResetConfirmView	password_reset_confirm
/accounts/reset/done/	django.contrib.auth.views.PasswordResetCompleteView	password_reset_complete
/accounts/signup/	accounts.views.SignUp	signup
/admin/	django.contrib.admin.sites.index	admin:index
/admin/<app_label>/	django.contrib.admin.sites.app_index	admin:app_list
/admin/auth/group/	django.contrib.admin.options.changelist_view	admin:auth_group_changelist
/admin/auth/group/<path:object_id>/	django.views.generic.base.RedirectView	
/admin/auth/group/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:auth_group_change
/admin/auth/group/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:auth_group_delete
/admin/auth/group/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:auth_group_history
/admin/auth/group/add/	django.contrib.admin.options.add_view	admin:auth_group_add
/admin/auth/group/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:auth_group_autocomplete
/admin/auth/user/	django.contrib.admin.options.changelist_view	admin:auth_user_changelist
/admin/auth/user/<id>/password/	django.contrib.auth.admin.user_change_password	admin:auth_user_password_change
/admin/auth/user/<path:object_id>/	django.views.generic.base.RedirectView	
/admin/auth/user/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:auth_user_change
/admin/auth/user/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:auth_user_delete
/admin/auth/user/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:auth_user_history
/admin/auth/user/add/	django.contrib.auth.admin.add_view	admin:auth_user_add
/admin/auth/user/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:auth_user_autocomplete
/admin/authtoken/token/	django.contrib.admin.options.changelist_view	admin:authtoken_token_changelist
/admin/authtoken/token/<path:object_id>/	django.views.generic.base.RedirectView	
/admin/authtoken/token/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:authtoken_token_change
/admin/authtoken/token/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:authtoken_token_delete
/admin/authtoken/token/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:authtoken_token_history
/admin/authtoken/token/add/	django.contrib.admin.options.add_view	admin:authtoken_token_add
/admin/authtoken/token/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:authtoken_token_autocomplete
/admin/jsi18n/	django.contrib.admin.sites.i18n_javascript	admin:jsi18n
/admin/login/	django.contrib.admin.sites.login	admin:login
/admin/logout/	django.contrib.admin.sites.logout	admin:logout
/admin/news/post/	django.contrib.admin.options.changelist_view	admin:news_post_changelist
/admin/news/post/<path:object_id>/	django.views.generic.base.RedirectView	
/admin/news/post/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:news_post_change
/admin/news/post/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:news_post_delete
/admin/news/post/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:news_post_history
/admin/news/post/add/	django.contrib.admin.options.add_view	admin:news_post_add
/admin/news/post/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:news_post_autocomplete
/admin/password_change/	django.contrib.admin.sites.password_change	admin:password_change
/admin/password_change/done/	django.contrib.admin.sites.password_change_done	admin:password_change_done
/admin/r/<int:content_type_id>/<path:object_id>/	django.contrib.contenttypes.views.shortcut	admin:view_on_site


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
