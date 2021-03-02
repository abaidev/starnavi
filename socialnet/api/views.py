from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from socialnet.models import Post
from socialnet.api.base import serializers as base_serializers
from socialnet.api.v1 import serializers as v1_serializers
from socialnet.api.v2 import serializers as v2_serializers
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

################## API for User model and authentication ##################
class UserSignupAPIView(CreateAPIView):
    serializer_class = base_serializers.UserSignupSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = base_serializers.UserSignupSerializer
    queryset = User.objects.all()
    lookup_field = 'email'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


################## API FOR POST MODEL ##################
class PostAPIView(ListCreateAPIView):
    # serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.version == '1.0':
            return v1_serializers.PostSerializerV1
        elif self.request.version == '2.0':
            return v2_serializers.PostSerializerV2
        return base_serializers.PostSerializer


class PostRUDAPIView(RetrieveUpdateDestroyAPIView):
    # serializer_class = base_serializers.PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.version == '1.0':
            return v1_serializers.PostSerializerV1
        elif self.request.version == '2.0':
            return v2_serializers.PostSerializerV2
        return base_serializers.PostSerializer


