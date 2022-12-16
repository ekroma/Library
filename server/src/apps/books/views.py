from rest_framework import filters
from django_filters import rest_framework as rest_filter
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwner
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .models import Books, Genre, UserBookRating, UserBookState
from . import serializers


class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    filter_backends = [filters.SearchFilter, rest_filter.DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'user__username']
    filterset_fields = ['genre']
    ordering_fields = ['genre']

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookListSerialiers
        return serializers.BookSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        if self.action in ['create', 'like']:
            self.permission_classes = [permissions.IsAuthenticated]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

class GenreView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class RatingViewSet(ModelViewSet):
    queryset = UserBookRating.objects.all()
    serializer_class = serializers.UserBookRatingSerializer


class BookStateViewSet(ModelViewSet):
    queryset = UserBookState.objects.all()
    serializer_class = serializers.UserBookStateSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)