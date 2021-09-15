from django.contrib import admin

from API.models import CharacterModel, QuoteModel


admin.site.register((CharacterModel, QuoteModel))
