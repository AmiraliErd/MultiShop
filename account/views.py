from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views import View
import ghasedakpack
from random import randint
from .forms import LoginForm, OtpLoginForm, CheckOtpForm, AddressCreationForm
from .models import Otp, User
# from django.utils.crypto import get_random_string
from uuid import uuid4

SMS = ghasedakpack.Ghasedak("480bd6910083678001fe43ac851d65bf818538945df6cfccba3c55ec6671af32")


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect("/")
            else:
                form.add_error("username", "Invalid user data")
        else:
            form.add_error("username", "Invalid data")

        return render(request, 'account/login.html', {'form': form})


class OtpLoginView(View):
    def get(self, request):
        form = OtpLoginForm
        return render(request, 'account/otp_login.html', {'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification({'receptor': cd['phone'], 'type': '1', 'template': 'randcode', 'param1': randcode})
            token = str(uuid4()) #get_random_string(length=100)
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error('phone', 'Invalid data')

        return render(request, 'account/otp_login.html', {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                otp.delete()
                return redirect('/')
            else:
                form.add_error('code', 'Invalid code')

        else:
            form.add_error('code', 'Invalid code')

        return render(request, 'account/check_otp.html', {'form': form})


class AddAddressView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/add_address.html', {'form': form})

    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

        return render(request, 'account/add_address.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')
