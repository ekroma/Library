from django.urls import path, include
from apps.comments.urls import urlpatterns as comment_urls
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RatingViewSet, BookStateViewSet

router = DefaultRouter()
router.register('books', BookViewSet, 'books')
router.register('user/book/states', BookStateViewSet)
router.register('user/book/rating', RatingViewSet)


urlpatterns = [
    path('books/<slug:slug>/comments/', include(comment_urls))
] + router.urls
