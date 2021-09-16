import json, requests

from rest_framework import permissions, status, views
from rest_framework.response import Response

from API.models import QuoteModel

from API.lib.headers import request_headers, BASE_URL


class FavoriteQuote(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id, pk):
        owner = request.user
        api_request = requests.get(
            BASE_URL+'quote/'+pk, headers=request_headers())
        api_response = json.dumps(api_request.json())

        db_record = QuoteModel.objects.filter(quote_id = pk)
        if db_record:
            return Response({"success":False, "message":"quote is already made a favorite"}, status=status.HTTP_400_BAD_REQUEST)

        data = json.loads(api_response).get('docs')[0]
        quote_id = data.get('_id')
        dialogue = data.get('dialog', '')
        movie = data.get('movie', '')
        character = data.get('character', '')
        favorite_character = str(id)

        new_quote = QuoteModel.objects.create(quote_id=quote_id, dialogue=dialogue,movie=movie, character=character, favorite_character=favorite_character)
        new_quote.owner.add(owner)
        new_quote.save()
        return Response({"success": True, "message": "favorite character added"}, status=status.HTTP_201_CREATED)
