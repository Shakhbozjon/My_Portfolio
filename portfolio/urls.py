from django.urls import path
from .views import IndexView, HomePageView, ContactPageView


urlpatterns = [
    # path('', IndexView.as_view(), name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('contact_me', ContactPageView.as_view(), name='contact')
]