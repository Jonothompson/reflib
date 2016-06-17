from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LibraryBaseView.as_view(), name="library_home"),
    url(r'^user-home/', views.UserLandingView.as_view(), name="user_home"),
]
