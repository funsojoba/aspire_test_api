from django.urls import path
from .views.characters.all_characters import GetCharacters


urlpatterns = [
    path('characters', GetCharacters.as_view(), name="characters")
]
