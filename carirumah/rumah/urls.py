from django.urls import path

from .views import (
    property_detail, 
    property_list, 
    property_create,
    property_search,
)

urlpatterns = [
    path('', property_list),
    path('create/', property_create),
    path('<int:id>/', property_detail),
    path('search/', property_search),
]
