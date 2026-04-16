from django.urls import path
from .views import *

urlpatterns = [
    path('users/', users, name='users'),
    path('user/<int:pk>/', user_detail, name='users'),
    path('user_create/', create_user, name='user_create'),
    path('barbers/', barbers, name='barbers'),
    path('barber/<int:pk>/', barber_detail, name='barbers'),
    path('barber_create/', create_barber, name='create_barber'),
    path('barber_update/<int:pk>/', update_barber, name='update_barber'),
    path('barber_delete/<int:pk>/', delete_barber, name='delete_barber'),
    path('service/<int:pk>', service_detail, name='service'),
    path('service_create/', create_service, name='create_service'),
    path('service_update/<int:pk>/', update_service, name='update_service'),
    path('service_delete/<int:pk>/', delete_service, name='delete_service'),
    path('service_category_detail/<int:pk>/', service_category_detail, name='service_category_detail'),
    path('service_category_create/', create_service_category, name='create_service_category'),
    path('service_category/',service_category, name='service_category'),
    path('service_category_update/<int:pk>/',update_service_category, name='service_category_update'),


]
