import requests, json
from django.http import HttpResponse
from rest_framework import views, permissions

from API.lib.headers import request_headers, BASE_URL



class GetCharacters(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        api_request = requests.get(BASE_URL+'character', headers=request_headers())
        data = json.dumps(api_request.json())
        return HttpResponse(data, content_type='application/json')

