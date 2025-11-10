# users/admin_auth.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class AdminTokenObtainPairView(TokenObtainPairView):
    """
    Use this view at /api/admin/login/ to only allow admin role.
    Post: { "username": "...", "password": "..." }
    """
    def post(self, request, *args, **kwargs):
        res = super().post(request, *args, **kwargs)
        if res.status_code != 200:
            return res
        # check role
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "No active account found with the given credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        if user.role != 'admin':
            return Response({"detail": "Not an admin"}, status=status.HTTP_403_FORBIDDEN)
        return res

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_profile(request):
    if getattr(request.user, 'role', None) != 'admin':
        return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
