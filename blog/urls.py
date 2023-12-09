from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [

    path('', PostList.as_view(),name='blog-list'),
    path('<uuid:pk>/',PostDetail.as_view(),name='blog-detail')
]


