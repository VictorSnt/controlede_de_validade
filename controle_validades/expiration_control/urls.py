from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listagem-de-validades/", views.expiration_list, name="expiration_list"),
    path("registrar-validade/", views.expiration_form, name="expiration_form"),
    path("seed/", views.seed_db, name="seed_db")
]