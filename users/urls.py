from django.urls import path
from .import views

urlpatterns = [
    path(r'', views.singup, name='singup'),
    path('login/', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_page, name='logout'),
    path('cart/', views.cart_page, name='cart'),
]