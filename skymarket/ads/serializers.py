from rest_framework import serializers

from ads.models import Ad
from ads.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source="id", required=False)
    ad_id = serializers.IntegerField(source="ad.id", required=False)
    author_id = serializers.IntegerField(source="ad.author.id", required=False)
    author_last_name = serializers.CharField(source="ad.author.last_name", required=False)
    author_first_name = serializers.CharField(source="ad.author.first_name", required=False)
    author_image = serializers.CharField(source="ad.author.image", required=False)

    class Meta:
        model = Comment
        exclude = ["id", "ad", "author"]


class AdSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source="id")

    class Meta:
        model = Ad
        exclude = ["id", 'created_at', "author"]


class AdDetailSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    pk = serializers.IntegerField(source="id", required=False)
    author_id = serializers.IntegerField(source="author.id", required=False)
    author_last_name = serializers.CharField(source="author.last_name", required=False)
    author_first_name = serializers.CharField(source="author.first_name", required=False)
    phone = serializers.CharField(source="author.phone", required=False)

    class Meta:
        model = Ad
        exclude = ["id", 'created_at']
