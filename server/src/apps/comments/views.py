from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import CommentSerializer, CommentCreateSerializer
from .permissions import IsAuthorOrReadOnly
from apps.books.models import Books
from .models import Comments


class ManageCommentsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    lookup_field = 'id'

    def get_queryset(self, **kwargs):
        queryset = Comments.objects.filter(id=self.kwargs['id'])
        return queryset


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        book_pk = self.kwargs["slug"]
        book = get_object_or_404(Books, pk=book_pk)
        return serializer.save(author=self.request.user, book=book)


@api_view(['GET', 'POST'])
def CommentLikeView(request, **kwargs):
    comment = get_object_or_404(Comments, id=kwargs.get("id"))
    user = request.user
    if user.is_authenticated:
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
    data = {
        'likes': comment.count_likes()
    }
    return Response(data)


class CommentsListView(APIView):
    def get(self, request, **kwargs):
        book = get_object_or_404(Books, pk=kwargs["slug"])
        comments = Comments.objects.filter(book=book)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
















