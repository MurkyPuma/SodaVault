from django import forms
from . import models


class Create(forms.ModelForm):
    class Meta:
        model = models.Drink
        fields = [
            "name",
            "alcoholic",
            "type",
            "thumbnail",
            "glass",
            "category",
            "ingredient1",
            "ingredient2",
            "ingredient3",
            "ingredient4",
            "ingredient5",
            "ingredient6",
            "ingredient7",
            "ingredient8",
            "ingredient9",
            "measurement1",
            "measurement2",
            "measurement3",
            "measurement4",
            "measurement5",
            "measurement6",
            "measurement7",
            "measurement8",
            "instructions",
        ]
