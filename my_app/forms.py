from django import forms
from django.views.generic import TemplateView


class MessageForm(TemplateView):
    template_name = 'my_app/message_form.hmml'
