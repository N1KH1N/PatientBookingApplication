from django.urls import path
from bookingweb import views

urlpatterns = [
    path("",views.IndexView.as_view(),name="home"),
]