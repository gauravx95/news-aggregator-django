from django.urls import path
from newsaggr import views


urlpatterns = [
    path('', views.index, name="home"),
]
