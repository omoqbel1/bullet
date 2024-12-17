from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('products/', views.products),
    path('customers/', views.customer),
    path('quote/', views.quote),
    path('thankyou/', views.thankyou),
    path('services/', views.services),
    path('about/', views.about),
    path('privacy/', views.privacy),
]
