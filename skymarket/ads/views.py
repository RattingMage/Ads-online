from rest_framework import pagination, viewsets, mixins

from ads.models import Ad

from ads.serializers import AdSerializer
from ads.serializers import AdDetailSerializer
from ads.serializers import CommentSerializer
from ads.models import Comment


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    # serializer_class = AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "create" or self.action == "partial_update":
            return AdDetailSerializer
        return AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    pagination_class = AdPagination
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad=self.kwargs.get("ad_pk"))

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs.get("ad_pk"))
