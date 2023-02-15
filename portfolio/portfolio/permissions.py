from rest_framework import permissions


class AuthenticatedPermissions(permissions.BasePermission):
    """Checking if the user is authorized."""

    def has_permission(self, request, view):
        return request.user.is_authenticated
