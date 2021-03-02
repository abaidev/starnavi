from socialnet.api.base import serializers as base_serializers

class PostSerializerV2(base_serializers.PostSerializer):
    class Meta(base_serializers.PostSerializer.Meta):
        fields = ["title", "id"]
