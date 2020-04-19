from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request, 'base.html')


def resume(request):
    return render(request, 'resume.html')


def message(request):
    return render(request, 'my_app/message_form.html')


def projects(request):
    return render(request, 'resume.html')


def send_message(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            save_it = form.save(commit=False)
            # username = form.cleaned_data.get('name')
            # user_email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            msg = form.cleaned_data.get('message')

            from_mail = settings.EMAIL_HOST_USER
            to_list = [save_it.email, settings.EMAIL_HOST_USER]

            send_mail(subject, msg, from_mail, to_list, fail_silently=True)

            message.success(request, 'Thank you for you response')
            return HttpResponseRedirect('/thank-you/')

    else:
        form = UserCreationForm()

    return render(request, 'my_app/message_form.html', {'form': form})
