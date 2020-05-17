from rest_framework.permissions import IsAuthenticated


class UserAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action == 'signup':
            return True
        return bool(request.user and request.user.is_authenticated)
