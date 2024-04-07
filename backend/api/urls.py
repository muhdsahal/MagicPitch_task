from django.urls import path
from .views import UserRegisterView,UserDetailsView,UserReferralsView
urlpatterns = [
    path('user_register/',UserRegisterView.as_view(),name='user_register'),
    path('user_details/',UserDetailsView.as_view(),name='user_details'),
    path('referrals/',UserReferralsView.as_view(),name='referrals')
]
