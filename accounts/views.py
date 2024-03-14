from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Account
from drinks.models import Drink
from django.shortcuts import get_object_or_404

# Create your views here.


def favourites(request):
    return render(request, "accounts/favourites.html")


@require_POST
def toggle_favourite(request, drink_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)
    drink = get_object_or_404(Drink, pk=drink_id)
    favorite, created = Account.objects.get_or_create(user=request.user, drink=drink)
    if not created:
        favorite.delete()  # Remove the favorite if it already existed
        return JsonResponse({"liked": False})
    return JsonResponse({"liked": True})


def recent(request):
    recent = Account.objects.all().order_by("date")
    return render(request, "accounts/recent.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("homepage")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect("homepage")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("homepage")


# @login_required(login_url="accounts:login")
# def create(request):
#     if request.method == "POST":
#         form = forms.Create(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             return redirect("drinks")
#     else:
#         form = forms.Create()
#     return render(request, "accounts/create.html", {"form": form})
