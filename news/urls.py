from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     # ex: /polls/5/
    path('<int:post_id>/', views.show, name='show'),
    # ex: /polls/5/edit/
    path('<int:post_id>/results/', views.edit, name='edit'),
    # ex: /polls/5/update/
    path('<int:post_id>/update/', views.update, name='update'),
]