from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow Users to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS = List objects and create new objects
            # We want to allow users to see
            # the profile of other users
            return True

        # Boolean Return True if user editing
        # is trying to edit his own profile
        return obj.id == request.user.id
