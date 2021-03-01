from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from socialnet.models import Post
from .serializers import (UserSignupSerializer, PostSerializer)
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

################## API for User model and authentication ##################
class UserSignupAPIView(CreateAPIView):
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
    lookup_field = 'email'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


################## API FOR POST MODEL ##################
class PostAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


