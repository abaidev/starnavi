from django.urls import path, include
from . import views

app_name = 'socialnet'

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('account/', UserView.as_view(), name='login'),
]