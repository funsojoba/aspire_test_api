from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response

from API.serializers.user_serializer import UserSerializer


class SignUpView(views.APIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})
