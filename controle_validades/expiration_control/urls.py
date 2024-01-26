
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listagem-de-validades/", views.display_expirations, name="display_expirations"),
    path("registrar-validade/", views.add_expiration, name="add_expiration"),

]