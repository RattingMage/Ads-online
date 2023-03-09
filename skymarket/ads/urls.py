from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet
from ads.views import CommentViewSet

# TODO настройка роутов для модели

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet, basename="ads")

comments_router = SimpleRouter()
comments_router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("ads/<int:pk>/", include(comments_router.urls)),
]
