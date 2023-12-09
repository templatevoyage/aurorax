from django.shortcuts import render
from django.views import generic

from .models import Post, Category


class PostList(generic.ListView):
    model = Post 
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.request.GET.get('category')
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    