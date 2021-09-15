import uuid

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class CharacterModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    owner = models.ManyToManyField(User)
    character_id = models.CharField(max_length=256)
    height = models.CharField(max_length=245, blank=True, null=True)
    race = models.CharField(max_length=245, blank=True, null=True)
    gender = models.CharField(max_length=245, blank=True, null=True)
    spouse = models.CharField(max_length=245, blank=True, null=True)
    death = models.CharField(max_length=245, blank=True, null=True)
    realm = models.CharField(max_length=245, blank=True, null=True)
    hair = models.CharField(max_length=245, blank=True, null=True)
    name = models.CharField(max_length=245, blank=True, null=True)
    wikiUrl = models.CharField(max_length=245, blank=True, null=True)

    def __str__(self):
        return self.name

class QuoteModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    owner = models.ManyToManyField(User)
    quote_id = models.CharField(max_length=256)
    dialogue = models.CharField(max_length=245, blank=True, null=True)
    movie = models.CharField(max_length=245, blank=True, null=True)
    character = models.CharField(max_length=245, blank=True, null=True)
