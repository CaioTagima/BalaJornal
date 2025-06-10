from django.shortcuts import render, redirect
from ..forms.userdetail_forms import UserDetailForm


def user_detail(request):
    if not request.user.is_authenticated:
        return redirect('user_signup')  
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.user = request.user 
            detail.save()
            return redirect('home')
    else:
        form = UserDetailForm()
    return render(request, 'registration/user_detail_registration.html', {'form': form})