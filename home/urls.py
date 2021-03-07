from django.urls import path
from .views import home_view,save_data,delete_data,edit_data
urlpatterns = [
    path('',home_view,name='home_view'),
    path('save/',save_data,name='save'),
    path('delete/',delete_data,name='delete'),
    path('edit/',edit_data,name='edit'),
]