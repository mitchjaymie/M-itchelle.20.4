from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")

def About(request):
    return render(request,"About Us.html")

def contact(request):
    return render(request,"Contact Us")
def location(request):
    return render(request,"location.html")
