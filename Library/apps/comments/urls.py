from django.urls import path
from .views import (CommentsListView, CommentCreateView,
                    ManageCommentsView, CommentLikeView)

urlpatterns = [
    path('', CommentsListView.as_view(), name='comment'),
    path('add/', CommentCreateView.as_view(), name='add-comment'),
    path('<int:id>/', ManageCommentsView.as_view(), name='manage-comment'),
    path('<int:id>/like/', CommentLikeView, name='like'),
]

