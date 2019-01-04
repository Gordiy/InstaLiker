from django.urls import path
from liker import views


urlpatterns = [
   path('', views.set_to_admin, name='user'),
]
