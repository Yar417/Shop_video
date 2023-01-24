from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь, {username} создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html',
                  {'title': 'Регистрация',
                   'form': form
                   })


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        updateUserForm = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profileUpdateForm = ProfileUpdateForm(
            request.POST,
            instance=request.user.profile)

        if profileForm.is_valid() and updateUserForm.is_valid() and profileUpdateForm.is_valid():
            profileForm.save()
            updateUserForm.save()
            profileUpdateForm.save()

            messages.success(request, f'Аккаунт обновлен')
            return redirect('profile')

    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'profileUpdateForm': profileUpdateForm
    }

    return render(request, 'users/profile.html', data)
