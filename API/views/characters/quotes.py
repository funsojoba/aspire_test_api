import requests, json

from django.http import HttpResponse
from rest_framework import views, permissions

from API.lib.headers import request_headers, BASE_URL


class Quote(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        api_request = requests.get(
            BASE_URL+'quote', headers=request_headers())
        data = json.dumps(api_request.json())
        return HttpResponse(data, content_type='application/json')
