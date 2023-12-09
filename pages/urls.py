from django.urls import path

from .views import (
    HomeView,
    ContactUsView,
    AboutUsView,
    TermsOfServiceView,
    PrivacyPolicyView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("contact/", ContactUsView.as_view(), name="contact"),
    path("privacy-policy/", PrivacyPolicyView.as_view(), name="privacy"),
    path("terms-of-service/", TermsOfServiceView.as_view(), name="terms_of_service"),
]
