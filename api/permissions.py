from rest_framework import permissions

class IsTrainerOrOwnerOrReadOnly(permissions.BasePermission):
    """
    - Trainers: Django is_staff users -> full access
    - Trainees: can view assigned projects and update their own assigned project
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated and request.user.is_staff
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff or obj.assigned_to == request.user
        if request.user.is_staff:
            return True
        if view.action in ['update', 'partial_update']:
            return obj.assigned_to == request.user
        return False
