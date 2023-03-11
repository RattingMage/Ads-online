from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ads.models import Ad
from ads.models import Comment

from ads.serializers import AdSerializer
from ads.serializers import AdDetailSerializer
from ads.serializers import CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


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

    @action(detail=False, methods=["get"])
    def me(self, request):
        pk = self.request.user.pk
        if pk is None:
            return Response("Unauthorized", status=401)
        ads = Ad.objects.filter(author=self.request.user)

        page = self.paginate_queryset(ads)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(ads, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    pagination_class = AdPagination
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad=Ad.objects.get(id=self.kwargs.get("ad_pk")))

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs.get("ad_pk"))
