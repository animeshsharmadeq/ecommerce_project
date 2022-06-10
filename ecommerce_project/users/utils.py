from django.core.mail import send_mail
from ecommerce_project.settings import SITE_BASE_URL


def send_approval_email(request, emailto, user):
    '''This is the send_approval_email function.

    It helps in sending approval mails to admin.
    '''
    msg = "A new shop user has signed up. To approve the request please visit this" + \
        f"link, {SITE_BASE_URL}/users/approval_requests/{user.id}"
    send_mail("Approval Request", msg, request.POST["email"], [emailto])
