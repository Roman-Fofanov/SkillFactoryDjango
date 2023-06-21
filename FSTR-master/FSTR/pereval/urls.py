from django.urls import path

from .views import CreateListView, RetrieveUpdateView


urlpatterns = [
    path('', CreateListView.as_view(), name='create-list'),
    path('<int:pk>/', RetrieveUpdateView.as_view(), name='retrieve-update'),
]
