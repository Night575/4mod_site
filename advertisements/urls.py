from django.urls import path
from .views import index, top_sellers, post_adv

urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', top_sellers, name="sellers"),
    path('post-adv/', post_adv, name="advertisement"),
]
