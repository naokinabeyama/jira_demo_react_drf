from rest_framework import permissions



class OwnerPermission(permissions.BasePermission):
    # owner.idとrequest.idが一緒なら更新削除の許可
    def has_object_permission(self, request, view, obj):
        # SAFE_METHOD == getメソッド
        # SAFE_METHODならpermissionを許可する
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.id == request.user.id 
        