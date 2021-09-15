from django.urls import path
from rest_framework.authtoken import views

from .views.characters.all_characters import GetCharacters
from .views.characters.character_quote import CharacterQuote
from .views.characters.character import Character
from .views.characters.quotes import Quote
from .views.authenticate.signup import SignUpView
from .views.characters.favorite_character import FavoriteCharacter

urlpatterns = [
    path('login', views.obtain_auth_token),
    path('signup', SignUpView.as_view(), name="sign_up"),

    path('characters', GetCharacters.as_view(), name="characters"),
    path('characters/<str:pk>/quote', CharacterQuote.as_view(), name="character_quote"),
    path('characters/<str:pk>', Character.as_view(), name="character_quote"),
    path('quote', Quote.as_view(), name="quote"),
    path('characters/<str:pk>/favorites', FavoriteCharacter.as_view(),
         name="favorite_character")
]
