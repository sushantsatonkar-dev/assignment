from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import fetch_open_ended_mutual_funds


User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class OpenEndedFundsView(APIView):
    """Fetch and display open-ended mutual fund schemes."""
    def get(self, request):
        funds_data = fetch_open_ended_mutual_funds()

        if "error" in funds_data:
            return Response(funds_data, status=status.HTTP_400_BAD_REQUEST)

        return Response(funds_data, status=status.HTTP_200_OK)
