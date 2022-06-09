from django.core.mail import send_mail
from django.http import HttpResponse
from ecommerce_project.settings import SITE_BASE_URL

def send_simple_email(request, emailto, user):
   msg = "A new shop user has signed up. To approve the request please visit this" + f"link, {SITE_BASE_URL}/users/approval_requests/{user.id}"
   send_mail("Approval Request", msg, request.POST["email"], [emailto])