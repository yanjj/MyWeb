# Create your views here.
from django.shortcuts import HttpResponseRedirect, render_to_response, RequestContext
from django.contrib import auth
from forms import ContactForm


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        return HttpResponseRedirect("/account/invalid/")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email', 'yanjj_haha@gmail.com'),
                    ['252204692@qq.com'],)

            return HttpResponseRedirect('/contact/thanks/')

    else:
        form = ContactForm(
                initial={'subject': "I love your site!"})

    return render_to_response('account/contact_form.html', {'form': form}, RequestContext(request))
