from API.models import CharacterModel, QuoteModel
from API.serializers.quote_serializer import QuoteSerializer
from API.serializers.character_serializer import CharacterSerializer

from rest_framework import status, permissions, views
from rest_framework.response import Response



class FavoriteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        owner = request.user
        favorite_quotes = QuoteModel.objects.filter(owner=owner)
        serialized_quote = QuoteSerializer(favorite_quotes, many=True)

        favorite_character = CharacterModel.objects.filter(owner=owner)
        serialized_character = CharacterSerializer(favorite_character, many=True)
        return Response({"success":True, 
                        "favorite_quotes":serialized_quote.data, 
                        "favorite_characters":serialized_character.data}, status=status.HTTP_200_OK)