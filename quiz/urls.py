from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'quiz'

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'recommendation-books', views.RecommendationBookViewSet, basename='recommendation-books')

urlpatterns = []
urlpatterns += router.urls
