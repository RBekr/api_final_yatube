from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from posts.models import Comment, Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentsSerializer,
                          FollowSerializer,
                          GroupSerializer,
                          PostSerializer,)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('following__username', )

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(
                user=self.request.user,
            )

    def get_queryset(self):
        return self.request.user.follower.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post')
        )

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get('post'))


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )
