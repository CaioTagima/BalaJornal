from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.user_register_forms import UserSignupForm


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['user_pk'] = user.pk
            return redirect('home')
        form = UserSignupForm()
    return render(request, 'registration/user_signup.html', {'form': form})

