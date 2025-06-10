from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.user_register_forms import UserSignupForm


def user_register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.user = request.user 
            detail.save()
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'registration/user_registration.html', {'form': form})