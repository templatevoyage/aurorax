from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "home.html"

class PrivacyPolicyView(generic.TemplateView):
    template_name = 'pages/privacy_policy.html'

class TermsOfServiceView(generic.TemplateView):
    template_name = 'pages/terms_of_service.html'

class AboutUsView(generic.TemplateView):
    template_name = "pages/about_us.html"


class ContactUsView(generic.TemplateView):
    template_name = "pages/contact_us.html"
