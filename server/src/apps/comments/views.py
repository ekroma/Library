from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import CommentSerializer, CommentCreateSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Comments


class ManageCommentsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Comments.objects.filter(id=self.kwargs['id'])
        return queryset


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


@api_view(['GET', 'POST'])
def CommentLikeView(request, id):
    comment = get_object_or_404(Comments, id=id)
    user = request.user
    like = False
    if user.is_authenticated:
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            like = True
            comment.likes.add(user)
    data = {
        'like': like
    }
    return Response({"data": data})


class CommentsListView(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)















