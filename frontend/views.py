from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AddToWallet(TemplateView):

    template_name = "frontend/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auth_token'] = "Token e89449e31726f5cbb1b738a88cb0da6416edfa2b"
        return context
