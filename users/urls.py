from django.urls import path
from users.views import RegisterAPIView, LoginAPIView, LogoutAPIView, UserProfileAPIView, ChangePasswordAPIView

urlpatterns = [
    path("api/register/", RegisterAPIView.as_view(), name="register"),
    path("api/login/", LoginAPIView.as_view(), name="login"),
    path("api/logout/", LogoutAPIView.as_view(), name="logout"),
    path("api/profile/", UserProfileAPIView.as_view(), name="profile"),
    path("api/change-password/", ChangePasswordAPIView.as_view(), name="change-password"),
]
