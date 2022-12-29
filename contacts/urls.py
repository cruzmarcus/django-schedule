from django.urls import path
from contacts import views

urlpatterns = [
    path("", view=views.index, name="index"),
]
