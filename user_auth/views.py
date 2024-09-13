from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.db import DatabaseError
from .forms import RegistrationForm


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful. Welcome!")
                return redirect("home")
            except DatabaseError as db_error:
                messages.error(
                    request,
                    "An error occurred while creating your account. Please try again.",
                )
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, "user_auth/register.html", {"form": form})
