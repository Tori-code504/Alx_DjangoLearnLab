from rest_framework import viewsets, permissions, filters
from django.db.models import Count
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification
from rest_framework import status
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        # Annotate with comment_count for efficiency
        return (
            Post.objects
            .select_related("author")
            .annotate(comment_count=Count("comments"))
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        qs = Comment.objects.select_related("author", "post")
        post_id = self.request.query_params.get("post")
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # create notification
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

    return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({"detail": "You haven’t liked this post."}, status=status.HTTP_400_BAD_REQUEST)





