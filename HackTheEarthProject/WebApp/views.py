from django.shortcuts import render, redirect
from WebApp.forms import *
from WebApp.models import *

# Create your views here.

def login_required_check(view):
    def updated_view(request):
        try:
            if request.session["loged_in"] == True:
                return view(request)
            else:
                return redirect(login)
        except KeyError:
            return redirect(login)
    return updated_view


def index(request):
	return render(request, "WebApp\\index.html")

def login(request):
    errorMessage = ''
    if request.method == 'POST':
        user_input = loginForms(request.POST)
        if user_input.is_valid():
            entered_username = user_input.cleaned_data["username"]
            entered_password = user_input.cleaned_data["password"]
            if Users.objects.filter(username=entered_username):
                if Users.objects.filter(username=entered_username).filter(password=entered_password):
                    request.session['username'] = entered_username
                    request.session['loged_in'] = True
                    return redirect(index)
                else:
                    request.session['loged_in'] = False
                    errorMessage = 'Wrong password'
            else:
                request.session['loged_in'] = False
                errorMessage = 'No such account'

    return render(request, "WebApp\\login.html", {
        'loginForm': loginForms(),
        'errorMessage': errorMessage
    })