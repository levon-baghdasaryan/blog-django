from django.shortcuts import render

from .forms import CustomUserCreationForm


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()


    context = {'form': form}
    return render(request, 'accounts/register.html', context)
