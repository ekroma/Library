from django.urls import path
from .views import (CommentsListView, CommentCreateView,
                    ManageCommentsView, CommentLikeView)

urlpatterns = [
    path('', CommentsListView.as_view(), name='book-comments-list'),
    path('<int:id>/', ManageCommentsView.as_view(), name='book-comment-detail'),
    path('add/', CommentCreateView.as_view(), name='add-comment'),
    path('<int:id>/like/', CommentLikeView, name='like-comment')

]

