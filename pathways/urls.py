from django.urls import path
from pathways import views

urlpatterns = [
    path("", views.index, name="index"),
    path("destination", views.destination, name="destination"),
    path("index", views.logo, name="index"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("service", views.service, name="service"),
    path("FAQs", views.FAQs, name="FAQs"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login"),
    path("tfare", views.tfare, name="tfare"),
    path("user", views.user, name="user"),
    path("userdetail", views.userdetail, name="userdetail"),
    path("payment", views.payment, name="payment"),
    path("userbooking", views.userbooking, name="userbooking"),
    path("tbooking", views.tbooking, name="tbooking"),
    path("signUp", views.signUp, name="signUp"),




]

