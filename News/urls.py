from django.urls import path
from .views import *

urlpatterns = [
    path("home/", Home, name="home"),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
    path("category/", Category, name="category")
]