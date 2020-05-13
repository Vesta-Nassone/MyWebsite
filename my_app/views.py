from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect


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
        name = request.POST.get('Name')
        subject = request.POST.get('Subject')
        msg = request.POST.get('Message')
        print(name + subject + msg)
        if form.is_valid():
            form.save(commit=False)
            save_it = form.save(commit=False)
            # username = form.cleaned_data.get('Name')
            # user_email = form.cleaned_data.get('Email')
            # subject = form.cleaned_data.get('Subject')
            # msg = form.cleaned_data.get('Message')

            from_mail = name
            to_list = [save_it.email, settings.EMAIL_HOST_USER]

            send_mail(subject, msg, from_mail, to_list, fail_silently=True)

            message.success(request, 'Thank you for you response')
            return redirect("/base.html")
            # return HttpResponseRedirect('/thank-you/')

    else:
        form = UserCreationForm()

    return render(request, 'my_app/message_form.html', {'form': form})

# def send_m(response):
#     if response.method == "POST":
#         form = UserCreationForm()
#         if form.is_valid():
#             form.save()
#
#             return redirect("/base.html")
#         else:
#             form = UserCreationForm()
#     return render(response, "my_app/message_form.html", {'form', form})
