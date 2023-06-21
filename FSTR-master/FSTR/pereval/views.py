from rest_framework.response import Response
from rest_framework import mixins
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
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError("Status is not new")
            serializer.save()
            return Response({"state": 1, "message": "Success"})
        else:
            return Response({"state": 0, "message": serializer.errors})
