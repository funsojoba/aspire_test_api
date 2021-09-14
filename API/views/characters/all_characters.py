import requests
from rest_framework import views, status, permissions
from rest_framework.response import Response

from API.lib.headers import request_headers, BASE_URL



class GetCharacters(views.APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        api_request = requests.get(BASE_URL+'characters', headers=request_headers())
        print(api_request)
        return Response({"Onaga":"Onaga"})