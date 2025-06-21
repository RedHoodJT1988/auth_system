from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# This would send verification email to user
def send_verification_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = request.build_absolute_uri(
        reverse('verify-email', kwargs={'uidb64': uid, 'token': token})
    )

    subject = 'Verify Your Email Address'
    message = render_to_string('emails/verify_email.html', {'verification_link': verification_link, 'user': user})

    send_mail(subject, message, 'hello@email.com', [user.email])


