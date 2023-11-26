from django.urls import path
from . import views

urlpatterns = [
    path('test', views.testAPI),
    path('testpost', views.testPost)
]