from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("members/", views.members, name="members"),
    path("events/", views.events, name="events"),
    path("user_auth/", include("django.contrib.auth.urls")),
    path("purchase_ticket/", views.purchase_ticket, name="purchase_ticket"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
