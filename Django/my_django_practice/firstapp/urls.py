from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('firstapp/',views.first_view,name='first_view'),
    path('firstapp/details/<int:id>',views.details,name='details'),
    path('testing/',views.testing, name='testing'),
]