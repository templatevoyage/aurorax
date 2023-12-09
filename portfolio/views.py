from django.shortcuts import render
from django.views import generic

from .models import Portfolio, Category

class PortfolioList(generic.ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolios'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    

class PortfolioDetail(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
