from django.urls import path, include
from .views import UserViewSet


userList = UserViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

userDetail = UserViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("users/", userList, name="users"),
    path("users/<int:pk>/", userDetail, name="user"),
]