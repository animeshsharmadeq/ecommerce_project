'''This is the views.py file.

It contains the different views that are linked with particular urls.
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from allauth.account.utils import send_email_confirmation
from .models import User
from .utils import is_admin, send_approval_email
from .forms import ShopUserSignUpForm, UpdateUserDetails


def index(request):
    '''This is the index view.

    It is called for users/home url.
    '''
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/admin/')
        else:
            return render(request, 'users/home.html', {})
    else:
        return redirect('/accounts/login/')


def updateprofile(request):
    '''This is the updateprofile view.

    It is used while updating the user profile at users/updateprofile url.
    '''
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
        return render(request, 'users/updateprofile.html', {"form": form})


def shopsignup(request):
    '''This is the shopsignup view.

    It is used to register shopuser into the database.
    '''
    if request.method == 'POST':
        profile = User.objects.create_user(request.POST["email"], request.POST["password1"],
                                           request.POST["date_of_birth"], request.POST["gender"],
                                           request.POST["address"], "SHOPUSER",
                                           request.POST["name"], False, request.POST["shopname"])
        send_email_confirmation(
            request, profile, signup=True, email=request.POST["email"])
        send_approval_email(request, "superuser@yopmail.com", profile)
        return redirect('/accounts/confirm-email/')
    else:
        form = ShopUserSignUpForm()
        return render(request, "users/shopsignup.html", {"form": form})


def all_approval_requests(request):
    '''This is the all_approval_requests view.

    It is used to show all the approval requests by the admin.
    '''
    if is_admin(request.user):
        user_details = User.objects.filter(is_active=False , rejection_reason = "").values()
        return render(request, "users/request_list.html", {"user_details": user_details})
    else:
        return HttpResponse("Unauthorised access", status=401)


def user_approval_requests(request, user_id):
    '''This is the user_approval_requests view.

    It is used to show the approval request of a particular user.
    '''
    if is_admin(request.user):
        user_details = User.objects.get(id=user_id)
        return render(request, "users/request_details.html", {"user_details": user_details})
    else:
        return HttpResponse("Unauthorised access", status=401)


def admin_approval(request):
    '''This is the admin_appoval view.

    It is called when admin approves/rejects the request.
    '''
    user = User.objects.get(id=request.POST["user_id"])
    rejection_reason = request.POST["rejection_reason"]
    if rejection_reason == 'APPROVED':
        user.is_active = True
    else:
        user.rejection_reason = rejection_reason
        user.is_active =False
    user.save()
    return redirect('/users/approval_requests')


def shopusers(request):
    if is_admin(request.user):
        users_list = User.objects.filter(user_type="SHOPUSER", is_active = True).values()
        return render(request, "users/shopusers.html", {"users_list": users_list})
    else:
        return HttpResponse("Unauthorised access", status=401)