from rest_framework import serializers
from socialnet.api.base import serializers as base_app_serializers

# Post model SERIALIZERS
class PostSerializerV1(base_app_serializers.PostSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='pk', view_name='api:post-rud')
    class Meta(base_app_serializers.PostSerializer.Meta):
        fields = ['title', 'created', 'likes']
