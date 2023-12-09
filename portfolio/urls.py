from django.urls import path

from .views import PortfolioList, PortfolioDetail

urlpatterns = [
    path('',PortfolioList.as_view(),name='portfolio-list'),
    path('<int:pk>',PortfolioDetail.as_view(),name='portfolio-detail'),

]
