from django.urls import path
from imyvmstats import views


urlpatterns = [
    path("", views.accountListing, name="home"),
    path("imyvmstats/<name>", views.imyvmstats_there, name="imyvmstats_there"),
    path("about/", views.playerinfos, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("moneyDetail/", views.accountDetail, name="moneyDetail"),
]