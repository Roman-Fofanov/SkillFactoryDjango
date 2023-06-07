from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as df_filters

from .models import Pereval
from .serializers import PerevalSerializer


class PerevalFilter(df_filters.FilterSet):
    class Meta:
        model = Pereval
        fields = ['user__email']


class CreateListView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [df_filters.DjangoFilterBackend]
    filterset_class = PerevalFilter

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveUpdateView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if instance.status != 'new':
            raise ValidationError("Status is not new")

        self.perform_update(serializer)

        response_data = {"state": 1}

        return Response(response_data, status=status.HTTP_200_OK)
