from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User, Customer
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from account_module.forms import RegisterForm, LoginForm

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            name = register_form.cleaned_data.get('name')
            family = register_form.cleaned_data.get('family')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = Customer(
                    email=user_email,
                    is_active=True,
                    username=user_email,
                    first_name=name,
                    last_name=family,
                    is_hairstyle=False,
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)

class LoginView(View):
    def get(self, request):
        if request.session.session_key:
            return render(request, 'stylist/customerIndex.html', )
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        if user.is_hairstyle:
                            return redirect(reverse('stylist_page'))
                        else:
                            return redirect(reverse('posts_list'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login.html', context)


class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
