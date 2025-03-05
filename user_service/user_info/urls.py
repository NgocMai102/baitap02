from django.urls import path

from .views import UserInfoView, VerifyTokenView

urlpatterns = [
    path('user_infor/', UserInfoView.as_view(), name='user_info'),
    path('verify_token/', VerifyTokenView.as_view(), name='verify_token'),
]