from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    

    path('show',views.show), 

    #ex: /notifications/5/edit/
    path('edit/<int:id>', views.edit),
     # ex: /notifications/5/update/
    path('update/<int:id>', views.update), 
    path('delete/<int:id>', views.destroy),
    path('services', views.ServiceList.as_view()),
    path('services/<int:pk>/', views.ServiceDetail.as_view()),
]