from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_stylists, name='posts_list'),
    path('posts/<int:stylist_id>/', views.get_stylist, name='stylist_detail'),
    path('my-details/', views.stylist_view, name='stylist_page'),
    path('new_time/', views.new_time, name='new_time'),
    path('new_service/', views.new_service, name='new_service'),
    path('my_data/', views.my_data, name='my_data'),
]
