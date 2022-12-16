from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RatingViewSet, BookStateViewSet

router = DefaultRouter()
router.register('books', BookViewSet, 'books')
router.register('user/book/states', BookStateViewSet)
router.register('user/book/rating', RatingViewSet)


urlpatterns = [

] + router.urls
