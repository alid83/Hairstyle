from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logoutView.as_view(), name='logout_page'),
]
