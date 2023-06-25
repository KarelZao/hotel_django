from django.urls import path
from . import views

app_name = 'agents'

from property.views import property_detail
urlpatterns = [
    path('',views.agents_list, name='agents_list'),
]