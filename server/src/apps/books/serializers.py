from rest_framework import serializers
from .models import Books, Genre, BookCover, BookState, Rating


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCover
        fields = 'image', 


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Books
        fields = ('cover', 'title','genre', 'file', 'user')

    def create(self, validated_data):
        return super().create(validated_data)

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs


class BookListSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('slug','cover', 'title', 'genre', 'file')      


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name')


class CurrentBookDefault:
    requires_context = True

    def call(self, serializer_field):
        return serializer_field.context['book']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BookStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookState
        fields = '__all__'
