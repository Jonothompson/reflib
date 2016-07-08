from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.LibraryBaseView.as_view(), name="library_home"),
    url(r'^user-home/', views.UserLandingView.as_view(), name="user_home"),
    url(r'^user-creation/', views.AccountCreate.as_view(), name="user_creation"),
]
