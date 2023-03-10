from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from ads.views import AdViewSet
from ads.views import CommentViewSet

# TODO настройка роутов для модели

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet, basename="ads")

comments_router = routers.NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register("comments", CommentViewSet, basename="comments")

# ads_me_router = SimpleRouter()
# ads_me_router.register("ads_me", AdsMeView, basename="ads")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
]
