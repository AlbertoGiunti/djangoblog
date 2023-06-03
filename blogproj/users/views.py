from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, ProfileReadOnlyForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # check if form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully Created for {username}, Log In now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    form = ProfileReadOnlyForm(instance=user.profile)
    return render(request, 'users/profile.html', {'user': user, 'form': form})


@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        u_form = ProfileUpdateForm(request.POST, instance=user)
        p_form = ProfileReadOnlyForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', username=user.username)
    else:
        u_form = ProfileUpdateForm(instance=user)
        p_form = ProfileReadOnlyForm(instance=user.profile)
    return render(request, 'users/profile_update.html', {'u_form': u_form, 'p_form': p_form})

