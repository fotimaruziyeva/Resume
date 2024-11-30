from django.urls import path
from .views import home_view,about_view,ContactFormView,BlogListView,portfolio_view

urlpatterns = [
    path('', home_view, name='home-page'),
    path('about/', about_view, name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    # path('article/', article_view, name='article-page'),
    path('blog/',BlogListView.as_view(), name='blog-page'),
    path('portfolio/', portfolio_view, name='portfolio-page'),
]
