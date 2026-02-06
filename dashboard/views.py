from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Account created successfully! Please log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    return render(request, "dashboard/signup.html")

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # Redirect to home/dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "dashboard/login.html")

# Logout view
def logout_view(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    units = [5, 7, 6, 4, 8, 9, 3]
    return render(request,"dashboard/dashboard.html",{'labels': labels,
        'units': units
    })

def recommendations(request):
    recos = [
        "Switch to LED bulbs to save ₹500/month.",
        "Reduce AC usage by 1 hour/day → save 30 units.",
        "Use washing machine in off-peak hours to save cost."
    ]
    return render(request, 'dashboard/recommendations.html', {'recos': recos})

def bill_estimator(request):
    bill = None
    selected_appliance = None

    appliances = {
        "Fan": 75,
        "LED Bulb": 10,
        "Refrigerator": 150,
        "TV": 100,
        "Washing Machine": 500,
        "Air Conditioner": 1500,
        "Laptop": 65,
        "Microwave": 1200,
    }

    if request.method == "POST":
        selected_appliance = request.POST.get("appliance")
        wattage = appliances.get(selected_appliance, 0)  # dropdown se wattage le liya
        hours = float(request.POST.get("hours"))
        days = int(request.POST.get("days"))
        rate = float(request.POST.get("rate"))

        units = (wattage * hours * days) / 1000
        bill = units * rate

    return render(request, 'dashboard/bill_estimator.html', {
        "bill": bill,
        "appliances": appliances,
        "selected_appliance": selected_appliance
    })



@login_required
def profile_view(request):
    return render(request, 'dashboard/profile.html', {"user": request.user})
def charts(request):
    return render(request, "dashboard/charts.html")



@login_required
def ai_insights(request):
    # Dummy usage data (baad me DB se connect kar sakta hai)
    weekly_usage = random.randint(200, 600)
    avg_usage = 350

    insights = []

    if weekly_usage > avg_usage:
        insights.append("⚡ Your energy usage is above average this week.")
    else:
        insights.append("✅ Your energy usage is within the efficient range.")

    if weekly_usage > 500:
        insights.append("❄ High consumption detected. AC or heater overuse suspected.")

    if weekly_usage < 250:
        insights.append("🌱 Great job! You are conserving electricity effectively.")

    insights.append("💡 Tip: Switching to LED bulbs can reduce lighting cost by 70%.")

    return render(request, "ai_insights.html", {
        "usage": weekly_usage,
        "insights": insights
    })
