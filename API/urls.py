from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.urls import path
from rest_framework import permissions
from rest_framework.authtoken import views

from .views.characters.all_characters import GetCharacters
from .views.characters.character_quote import CharacterQuote
from .views.characters.character import Character
from .views.characters.quotes import Quote
from .views.authenticate.signup import SignUpView
from .views.characters.favorite_character import FavoriteCharacter
from .views.characters.favorite_quote import FavoriteQuote
from .views.characters.favorites import FavoriteView

schema_view = get_schema_view(
    openapi.Info(
        title="LOTR Characters API",
        default_version='v1',
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger',
                                        cache_timeout=0), name='schema-swagger-ui'),

    path('login', views.obtain_auth_token),
    path('signup', SignUpView.as_view(), name="sign_up"),

    path('characters', GetCharacters.as_view(), name="all_characters"),
    path('characters/<str:pk>/quote', CharacterQuote.as_view(), name="character_quote"),
    path('characters/<str:pk>', Character.as_view(), name="character"),
    path('quote', Quote.as_view(), name="quote"),
    path('characters/<str:pk>/favorites', FavoriteCharacter.as_view(),
         name="favorite_character"),
    path('characters/<str:id>/quotes/<str:pk>/favorites', FavoriteQuote.as_view(), name="favority_quote"),
    path('favorites', FavoriteView.as_view(), name="favorites")
]
