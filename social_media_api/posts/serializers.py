from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class CommentSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

    def create(self, validated_data):
        # author comes from request.user
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)
    # Optional: include comments inline (read-only). Comment out if you prefer separate requests.
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "author", "title", "content",
            "created_at", "updated_at",
            "comment_count",
            # "comments",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "comment_count"]

    def to_representation(self, instance):
        # annotate-friendly comment_count fallback
        rep = super().to_representation(instance)
        if rep.get("comment_count") is None:
            rep["comment_count"] = instance.comments.count()
        return rep

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)
