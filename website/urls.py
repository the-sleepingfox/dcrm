from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<str:pk>',views.customer_record, name='record'),
    path('delete_record/<str:pk>',views.delete_record, name='delete_record'),
    path('create_record/', views.create_record, name='create_record'),
]