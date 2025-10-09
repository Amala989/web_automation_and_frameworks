from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Expense, Category
from .forms import ExpenseForm, SignupForm


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "tracker/dashboard.html", {"expenses": expenses})


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("dashboard")
    else:
        form = ExpenseForm()
    return render(request, "tracker/add_expense.html", {"form": form})

@login_required
def manage_categories(request):
    categories = Category.objects.all()
    return render(request, "tracker/manage_categories.html", {"categories": categories})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after signup
            return redirect("dashboard")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist. Please sign up first.")
            return redirect("login")

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid password. Please try again.")

    return render(request, "registration/login.html")
