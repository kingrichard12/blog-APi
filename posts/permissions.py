from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #authenticated users only can see list view 
        if request.user.is_authenticated:
            return True 
        return False
    
    def has_object_permission(self, request, view, obj):
        #read permissions are allowed to any request so we'll always allow 
        #Get,Head, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        #write Permissions are only allowed to the author of the Post 
        return obj.author==request.user