from django.urls import path, include
from . import views

app_name = 'socialnet'

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('account/', views.UserProfileView.as_view(), name='account'),
]