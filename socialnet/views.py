from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (get_user_model, authenticate,
                                 login, logout)
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView
from django.views import View
from .forms import CreateUserForm, UserDetailChangeForm

User = get_user_model()

def index(request):
    return render(request, 'index.html', {})

def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in already')
        return redirect('socialnet:home')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socialnet:home')
    return render(request, "signup.html", {'form': form})


class UserLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are logged in already")
            return redirect("socialnet:home")
        return render(request, self.template_name, {})

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {email}")
            return redirect('socialnet:home')
        else:
            messages.warning(request, "Login credentials are incorrect")
        return redirect(request.META.get("HTTP_REFERER"))

@method_decorator(login_required(login_url="socialnet:login"), name='dispatch')
class UserProfileView(UpdateView,  DeleteView):
    login_url = 'socialnet:login'
    template_name = 'profile.html'
    form_class = UserDetailChangeForm
    initial = {}

    def get_object(self, queryset=None):
        email = self.request.user.email
        user = User.objects.get(email=email)
        return user

    def form_valid(self, form):
        user = User.objects.get(email=self.request.user.email)
        user.first_name, user.last_name = form.data.get('first_name'), form.data.get('last_name')
        user.save()
        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.delete()
        messages.info(request, "Your Account has been deleted")
        return redirect('socialnet:home')

class UserLogoutView(LogoutView, LoginRequiredMixin):
    login_url = 'socialnet:login'
    next_page = 'socialnet:login'
