from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from .forms import CreateUserForm
from django.contrib import messages


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account successfuly created for " + user)

            return redirect("login")

    context = {'form':form}
    return render(request, 'accounts/register.html', context)