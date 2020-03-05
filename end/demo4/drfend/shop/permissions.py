# Charlie
# date:2020/3/3 14:13
# file_name:permissions
from rest_framework import permissions


class CategorysPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class OrdersPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj, request.user)
        return obj.user == request.user
