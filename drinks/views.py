from django.http import JsonResponse
from django.http import HttpResponse
from .models import Drink
from accounts.models import Account
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
import requests
from django.conf import settings
from django.core.files.base import ContentFile
import uuid
import random
from PIL import Image
from django.contrib.postgres.search import SearchVector
import io
from rest_framework.pagination import PageNumberPagination


limitDisplay = 20 # Default number of drinks to display per page


@api_view(["GET", "POST"])
def drink_list(request, format=None):
    # get all drinks from the database
    # serialize them to json
    # return the json

    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def drink_info(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def homepage(request):
    return render(request, "homepage.html")


    
@api_view(["GET"])
def random_drinks(request):  # API function to get random drinks
    random = Drink.objects.order_by('?')
    limit = int(request.GET.get("limit", "")) # get the limit parameter from the request, no default
    start = int(request.GET.get("start", ""))
    queryset = random[start:start + limit]
    serializer = DrinkSerializer(queryset, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def search_drink_name(request):
    search_query = request.GET.get("q", "")
    limit = int(request.GET.get("limit", "")) # get the limit parameter from the request, no default
    start = int(request.GET.get("start", ""))

    if search_query:
        drinks = Drink.objects.annotate(search=SearchVector('name')).filter(search=search_query)
    queryset = drinks[start:start + limit]
    serializer = DrinkSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def search_drink_ingredient(request):
    search_query = request.GET.get("q", "")
    limit = int(request.GET.get("limit", "")) # get the limit parameter from the request, no default
    start = int(request.GET.get("start", ""))
    if search_query:
        drinks = Drink.objects.annotate(search=SearchVector
                                        ('ingredient1', 'ingredient2', 'ingredient3', 'ingredient4', 'ingredient5',
                                         'ingredient6', 'ingredient7', 'ingredient8', 'ingredient9'
                                         )).filter(search=search_query)
    queryset = drinks[start:start + limit]
    serializer = DrinkSerializer(queryset, many=True)
    return Response(serializer.data)


    

# def cocktails(request):
#     alcoholicDrinks = Drink.objects.filter(alcoholic="Alcoholic")
#     return render(request, "cocktails.html", {"drinks": alcoholicDrinks})


# def mocktails(request):
#     nonAlcoholicDrinks = Drink.objects.filter(alcoholic="Non alcoholic").order_by(
#         "name"
#     )
#     return render(request, "mocktails.html", {"drinks": nonAlcoholicDrinks})


def drinks(request):
    show_type = request.GET.get("show_alcoholic", "all")

    if request.user.is_authenticated:
        if show_type == "1":
            drinks = Drink.objects.filter(
                alcoholic="Alcoholic", author=None
            ) | Drink.objects.filter(alcoholic="Alcoholic", author=request.user)

        elif show_type == "0":
            drinks = Drink.objects.filter(
                alcoholic="Non alcoholic", author=None
            ) | Drink.objects.filter(alcoholic="Non alcoholic", author=request.user)

        else:
            drinks = Drink.objects.filter(author=None) | Drink.objects.filter(
                author=request.user
            )

    else:
        if show_type == "1":
            drinks = Drink.objects.filter(alcoholic="Alcoholic", author=None)
        elif show_type == "0":
            drinks = Drink.objects.filter(alcoholic="Non alcoholic", author=None)
        else:
            drinks = Drink.objects.filter(author=None)

    # Moved the return statement outside of the if-else blocks so it gets executed in all cases.
    return render(
        request,
        "drinks.html",
        {"drinks": drinks},
    )


# def drink_detail(request, id):
#     drink = Drink.objects.get(pk=id)

#     return render(request, "drinkDetail.html", {"drink": drink})


def drink_detail(request, id):
    drink = Drink.objects.get(pk=id)
    drink.save()  # Essencially a no-op, but it will call the save method and set the slug if it's not already set

    GPT_prompt = f"Create a photo-realistic image of an alcoholic drink presented in a clear {drink.glass}."
    GPT_prompt += f"The image should utilize a soft clay color palette, ensuring no parts of the drink resemble words or text - it is crucial."
    GPT_prompt += f"The drink should be elegantly simple, featuring specific ingredients listed in the drink's recipe: "

    if (
        (drink.thumbnail == "default.png")
        and drink.instructions
        and drink.author == None
        and drink.author == 1
    ):
        if drink.ingredient1 and drink.measurement1:
            GPT_prompt += f"{drink.ingredient1} adds a subtle hue to the liquid; "
        if drink.ingredient2 and drink.measurement2:
            GPT_prompt += f"{drink.ingredient2} which may alter the texture slightly;"
        if drink.ingredient3 and drink.measurement3:
            GPT_prompt += f"{drink.ingredient3}, "
        if drink.ingredient4 and drink.measurement4:
            GPT_prompt += f"{drink.ingredient4}, "
        if drink.ingredient5 and drink.measurement5:
            GPT_prompt += f"{drink.ingredient5}, "
        if drink.ingredient6 and drink.measurement6:
            GPT_prompt += f"{drink.ingredient6}, "
        if drink.ingredient7 and drink.measurement7:
            GPT_prompt += f"{drink.ingredient7}, "
        if drink.ingredient8 and drink.measurement8:
            GPT_prompt += f"{drink.ingredient8}, "
        if drink.ingredient9 and drink.measurement9:
            GPT_prompt += f"{drink.ingredient9} "
        GPT_prompt += (
            "each contributing to the overall aesthetic in a minimalistic way."
        )
        GPT_prompt += f"The {drink.glass} should be accurate and set against a neutral background to emphasize the drink itself"
        GPT_prompt += f"Pay particular attention to the garnishes as detailed in the instructions: {drink.instructions}."
        GPT_prompt += f"The focus should be on the clarity of the drink, the purity of the ice cubes,"
        GPT_prompt += f" and the overall sophistication of the presentation without any distractions."
        GPT_prompt += f"It is EXTREMELY important the image does NOT contain any text, writing, or logos."

        API_KEY = settings.OPENAI_API_KEY
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "dall-e-3",
            "prompt": GPT_prompt,
            "n": 1,  # Number of images to generate
            "size": "1024x1024",  # Image size
            "quality": "standard",
        }

        # Make the API request to generate the image
        response = requests.post(
            "https://api.openai.com/v1/images/generations", headers=headers, json=data
        )

        # Check if the API request was successful
        if response.status_code == 200:
            response_data = response.json()
            image_url = response_data["data"][0]["url"]

            # Download the generated image
            image_response = requests.get(image_url)
            # Assuming 'image_response' contains the successful response from the image download request
            if image_response.status_code == 200:
                # Generate a unique suffix for the filename
                # unique_suffix = uuid.uuid4().hex[:8]
                # filename = f"{drink.slug}_{unique_suffix}.png"
                filename = f"{drink.unique_slug}.png"

                # Create a ContentFile object from the image content
                image_content = ContentFile(image_response.content, name=filename)

                # Save this content directly to the Drink object's thumbnail field
                drink.thumbnail.save(filename, image_content, save=True)

    # Prepare the context for rendering the template, including the drink and image details
    context = {
        "drink": drink,
        "GPT_prompt": GPT_prompt,
        "image_url": drink.thumbnail.url if drink.thumbnail else None,
    }
    # Render and return the drink detail page with the provided context
    return render(request, "drinkDetail.html", context)


@login_required(login_url="accounts:login")
def create(request):
    if request.method == "POST":
        form = forms.Create(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("drinks")
    else:
        form = forms.Create()
    return render(request, "create.html", {"form": form})

