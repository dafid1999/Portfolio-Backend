from rest_framework import permissions

from .enum import UserType

class AdministrationPermissions(permissions.BasePermission):
    """Administration create, read, delete, update permissions."""

    def has_permission(self, request, view):
        """Administrator accesses to create, modify and delete members."""
        if not request.user.is_authenticated:
            return False
        if request.method in ["POST", "GET", "DELETE", "PUT", "PATCH"]:
            return request.user.user_type == UserType.ADMINISTRATOR or request.user.is_superuser
        return True


class UsersPermissions(permissions.BasePermission):
    """All users read, update permissions."""

    def has_permission(self, request, view):
        """All users accesses to read, modify and account detail."""
        if not request.user.is_authenticated:
            return False
        if request.method in ["GET", "PUT", "PATCH"]:
            return request.user
        return True
