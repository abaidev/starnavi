from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import *

app_name = 'api'

urlpatterns = [
    path('user/signup/', UserSignupAPIView.as_view(), name='user-signup'),
    path('user/token/', obtain_jwt_token, name='auth-token'),
    path('user/<str:email>/', UserRUDAPIView.as_view(), name='user-rud'),
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('posts/<slug:slug>/', PostRUDAPIView.as_view(), name='post-rud'),
]