from django.urls import path
from .views import shorten_url, redirect_to_original_url,short_url_list

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('short-url-list/', short_url_list, name='short_url_list'),
    path('<str:short_code>/', redirect_to_original_url, name='redirect_to_original_url'),
]
