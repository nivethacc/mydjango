
from django.conf.urls import url
from django.contrib import admin

from portfolioapp.views import HomeView,UserRegistrationFormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', UserRegistrationFormView.as_view()),
    url(r'^home/', HomeView.as_view()),
]
