from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
     # ex: /documents/5/
    # path('<int:document_id>/', views.show, name='show'),
    # # ex: /documents/5/edit/
    # path('<int:document_id>/edit/', views.edit, name='edit'),
    # # ex: /documents/5/update/
    # path('<int:document_id>/update/', views.update, name='update'),

    path('show',views.show), 

    #ex: /documents/5/edit/
    path('edit/<int:id>', views.edit),
     # ex: /documents/5/update/
    path('update/<int:id>', views.update), 
    path('delete/<int:id>', views.destroy),  

    path('documents', views.DocumentList.as_view()),
    path('documents/<int:pk>/', views.DocumentDetail.as_view()),
    path('approved', views.approved),
    path('disapproved', views.disapproved),
]