# Create your views here.
from django.shortcuts import HttpResponseRedirect
from django.contrib import auth


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        return HttpResponseRedirect("/account/invalid/")


def logout_out(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")
