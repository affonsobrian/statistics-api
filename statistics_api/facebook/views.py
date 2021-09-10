from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from .models import Post, PostHistory
from .serializers import PostSerializer, PostHistorySerializer
from .mixings import CreateOrUpdateIfExistsMixin

class PostViewSet(CreateOrUpdateIfExistsMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-updated_at")
    serializer_class = PostSerializer
    filterset_fields = ['user_id']
    update_data_pk_field = "post_id"
    lookup_field = "post_id"


class PostHistoryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PostHistory.objects.all().order_by("-created_at")
    filterset_fields = ['user_id', 'post_id']
    serializer_class = PostHistorySerializer
    filterset_fields = ['user_id', 'post_id', 'likes', 'created_at']

    @action(detail=False, methods=['get'])
    def month_average(self, request, *args, **kwargs):
        try:
            user_id = request.query_params["user_id"]
            queryset = PostHistory.objects.filter(user_id=user_id)
        except KeyError:
            queryset = PostHistory.objects.all()

        queryset = PostHistory.get_average_of_likes_from_past_thirty_days(queryset)
        return Response(queryset)
