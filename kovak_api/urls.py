from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from kovak_api.carshop import urls as car_urls
from kovak_api.users import urls as users_urls

urlpatterns = [
    path("", include(users_urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("car/", include(car_urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
