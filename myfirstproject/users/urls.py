from django.urls import path
from .views import user_create, user_login

urlpatterns = [
    path('create/', user_create, name='user-create'),
    path('login/', user_login, name='user-login'),  # Add this line
]
