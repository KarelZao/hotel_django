from django.urls import path
from . import views

app_name = 'about'

from property.views import property_detail
urlpatterns = [
    path('',views.aboutus, name='aboutus'),
]