from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index_user(response):
    form = UserCreationForm()
    return render(response, "user_signup/register.html", {"form": form })