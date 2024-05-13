from django.urls import path
from .views import concert_list, concert_detail

urlpatterns = [
    path('', concert_list, name='concert_list'),
    path('<int:concert_id>/', concert_detail, name='concert_detail'),
]
