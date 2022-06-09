from django.shortcuts import render, redirect
from .utils import send_simple_email
from .forms import ShopUserSignUpForm, UpdateUserDetails, CustomSignupForm
from .models import User
from allauth.account.utils import send_email_confirmation
from django.http import HttpResponse

def index(request):
    if(request.user.is_authenticated):
        if(request.user.is_staff):
            return redirect('/admin/')
        else:
            return render(request, 'users/home.html', {})
    else:
        return redirect('/accounts/login/')

def updateprofile(request):
    if request.method == 'POST':
        form = UpdateUserDetails(request.POST, instance=request.user)
        if form.is_valid():
            profile = User.objects.get(email=request.user.email)
            profile.name = form.cleaned_data['name']
            profile.gender = form.cleaned_data['gender']
            profile.address = form.cleaned_data['address']
            profile.date_of_birth = form.cleaned_data['date_of_birth']
            profile.save()
        return render(request, 'users/home.html', {})
    else:
        form = UpdateUserDetails(instance=request.user)
        return render(request, 'users/updateprofile.html', {"form":form})

def shopsignup(request):
    if request.method == 'POST':
        profile = User.objects.create_user(request.POST["email"], request.POST["password1"], request.POST["date_of_birth"], request.POST["gender"], request.POST["address"], "SHOPUSER", request.POST["name"], False, request.POST["shopname"])      
        send_email_confirmation(request, profile, signup=True, email=request.POST["email"])
        send_simple_email(request, "superuser@yopmail.com", profile)
        return redirect('/accounts/confirm-email/')
    else:
        form = ShopUserSignUpForm()
        return render(request, "users/shopsignup.html", {"form": form})

def all_approval_requests(request):
    if(request.user.is_authenticated):
        user_details = User.objects.filter(is_active=False).values()
        return render(request, "users/request_list.html", {"user_details": user_details})
    else:
        return HttpResponse("Unauthorised access",status=401)

def user_approval_requests(request, user_id):
    if(request.user.is_authenticated):
        user_details = User.objects.get(id=user_id)
        return render(request, "users/request_details.html", {"user_details":user_details})
    else:
        return HttpResponse("Unauthorised access",status=401)

def admin_approval(request):
    user = User.objects.get(id=request.POST["user_id"])
    user.is_active=True
    user.save()
    return redirect('/users/approval_requests')