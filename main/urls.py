from django.urls import path
from .views import home_page_view,  post_page_view, add_post


urlpatterns=[
    path('', home_page_view, name="home"),
    # path('contact/', contact_page_view, name="contact"),
    path('post/<int:blog_id>/' ,post_page_view, name="post"),
    path('add/', add_post, name="add_post")
]