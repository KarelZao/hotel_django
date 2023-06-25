from django.urls import path
from . import views

app_name = 'property'

from property.views import property_detail
urlpatterns = [
    path('',views.property_list, name='property_list'),
    path('<int:id>',views.property_detail, name='property_detail'),
]