from django.urls import path

from .views import CreateListView, RetrieveUpdateView


urlpatterns = [
    path('', CreateListView.as_view()),
    path('<int:pk>/', RetrieveUpdateView.as_view()),
]
