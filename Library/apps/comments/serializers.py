from rest_framework import serializers
from .models import Comments


class FilterCommentsListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('book', 'content', 'parent')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    replies = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentsListSerializer
        model = Comments
        fields = ("user", "content", "likes", "replies")






