from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "WebApp\\index.html")

def login(request):
	return render(request, "WebApp\\login.html", {
		"loginForm"
	})