from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'slug', 'unique_slug', 'alcoholic', 'type', 'thumbnail', 'glass', 'category', 'ingredient1', 'ingredient2', 'ingredient3', 'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7', 'ingredient8', 'ingredient9', 'measurement1', 'measurement2', 'measurement3', 'measurement4', 'measurement5', 'measurement6', 'measurement7', 'measurement8', 'measurement9', 'instructions', 'author']