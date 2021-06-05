from django.shortcuts import render

# Create your views here.

def index(request):
	var = 12
	return render(request, "WebApp\\index.html", {
		'var': var
	})