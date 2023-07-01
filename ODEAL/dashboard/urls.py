from django.urls import path

from . import views

app_name = 'dahsboard'

urlpatterns = [
    path('',views.index, name='index'),
]
