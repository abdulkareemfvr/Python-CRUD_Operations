from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('add_book', views.add_book, name='add_book'),
    path('update_book', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book,name="delete_book"),
    path('<int:id>/', views.update_book_details,name="update_book_details"),

]
