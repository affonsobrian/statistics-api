from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from rest_framework.request import Request

class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (IsUserOrReadOnly,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CreateUserSerializer
        return UserSerializer
