from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('details/<int:pk>', views.details_page, name='details')
]
