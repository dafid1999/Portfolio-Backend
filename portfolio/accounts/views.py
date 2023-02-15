from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

from .permissions import AdministrationPermissions, UsersPermissions
from .models import Uzytkownik
from .serializers import UzytkownikSerializer
from .models import UserType


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UsersPermissions,)
    serializer_class = UzytkownikSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser | user.user_type == UserType.ADMINISTRATOR:
            return Uzytkownik.objects.all()

    def get_object(self):
        obj = get_object_or_404(Uzytkownik.objects.filter(id=self.kwargs["pk"]))
        self.check_object_permissions(self.request, obj)
        return obj
