from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_view(request):
    user_form=UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'forms': user_form
    }
    return render(request, "accounts/register.html",context)

def logout_confirm(request):
    return render(request, "accounts/logout.html")