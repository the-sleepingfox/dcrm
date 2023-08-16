from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # Read
    path('record/<str:pk>',views.customer_record, name='record'),
    # Delete
    path('delete_record/<str:pk>',views.delete_record, name='delete_record'),
    # Create
    path('create_record/', views.create_record, name='create_record'),
    # Update
    path('update_record/<str:pk>', views.update_record, name='update_record'),
]