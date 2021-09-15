from django.db import models
import requests
import json
from django.http import HttpResponse

from rest_framework import views, permissions, status
from rest_framework.response import Response

from API.lib.headers import request_headers, BASE_URL
from API.models import CharacterModel


class FavoriteCharacter(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        owner = request.user
        api_request = requests.get(
            BASE_URL+'character/'+pk, headers=request_headers())
        api_response = json.dumps(api_request.json())

        data = json.loads(api_response).get('docs')[0]
        character_id = data.get('_id', '')
        height = data.get('heignt', '')
        race = data.get('race', '')
        gender = data.get('gender', '')
        spouse = data.get('spouse', '')
        death = data.get('death', '')
        realm = data.get('realm', '')
        hair = data.get('hair', '')
        name = data.get('name', '')
        wikiUrl = data.get('wikiUrl', '')
        new_favorite = CharacterModel.objects.create( character_id=character_id, height=height, race=race,
                                      gender=gender, spouse=spouse, death=death, realm=realm, hair=hair, name=name, wikiUrl=wikiUrl)
        new_favorite.owner.add(owner)
        new_favorite.save()
        return Response({"success": True, "message": "favorite character added"}, status=status.HTTP_201_CREATED)
