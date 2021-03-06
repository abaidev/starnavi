from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from socialnet.models import Post

User = get_user_model()

# USER MODEL SERIALIZERS
class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                    style={'input_type': 'password', 'placeholder': 'The Password please'})
    password2 = serializers.CharField(write_only=True, label="Confirm Password",
                                        style={'input_type': 'password', 'placeholder': 'Repeat Password please'})

    class Meta:
        model = User
        exclude = ['is_admin', 'is_active', 'last_login']

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                   first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

    def validate(self, data):
        email = data['email']
        password = data['password']
        password2 = data['password2']
        user_qs = User.objects.filter(Q(email=email)).distinct()
        if password != password2:
            raise ValidationError("Passwords don't match")
        elif len(user_qs) > 0:
            raise ValidationError("User with such email already exists")
        return data


# Post model SERIALIZERS
class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='pk', view_name="api:post-rud")
    user = UserSignupSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ["id", "user", "slug"]
        extra_kwargs = {"slug": {"required": False}, "image_cover": {"required": False}}
