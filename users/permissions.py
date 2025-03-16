from rest_framework.permissions import BasePermission


class IsModerators(BasePermission):
    """Проверка, является ли пользователь модератором."""
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderators").exists()


class IsOwner(BasePermission):
    """Проверка, является ли пользователь владельцем."""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsTeacher(BasePermission):
    """Проверка, является ли пользователь преподавателем."""
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Teachers").exists()
