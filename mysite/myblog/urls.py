from django.urls import path
from .views import list_view
#from .views import stub_view
from .views import detail_view

urlpatterns = [
    path('',list_view, name="blog_index"),
    #path('', stub_view, name="blog_index"),
    #path('posts/<int:post_id>/', stub_view, name="blog_detail"),
    path('posts/<int:post_id>/',detail_view, name="blog_detail"),
]