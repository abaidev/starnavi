from django.urls import path, include
from .views import index

app_name = 'socialnet'

urlpatterns = [
    path('', index, name='home'),
    # path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='login'),
    # path('account/', UserView.as_view(), name='login'),
]