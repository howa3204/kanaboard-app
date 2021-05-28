from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render

# Create your views here.

@login_required(login_url='authentication:login')
def contact(request):
    if request.method == "POST":
        subject = request.POST['subject']
        body = request.POST['body']
        from_email = ['support@kanaboard.com']
        reply_to = request.POST['reply_to']
        context = {'subject':subject,
                   'body':body,
                   'reply_to':reply_to,
                   }

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email='support@kanaboard.com',
            to=['support@kanaboard.com'],
            reply_to=[reply_to],
            headers={'username': request.user.username},
            )

        email.send(fail_silently=False)

        messages.success(request, "Message recieved! We'll get back to you shortly.")
        return render(request, 'contact/contact.html', context)

    else:
        context = {}
        return render(request, 'contact/contact.html', context)
