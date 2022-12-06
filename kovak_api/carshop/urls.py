from django.urls import include, path

from .views import CarView

urlpatterns = [
    path("api", CarView.as_view()),
]
