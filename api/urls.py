from django.urls import path
from . import views


urlpatterns = [
    path('',views.get_all_users),
    path('add/',views.add_user),
]
