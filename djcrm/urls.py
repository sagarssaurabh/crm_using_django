from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from leads.views import landing_view, LandingPageView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing'),
    path('leads/', include("leads.urls", namespace="leads")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name='logout-page'),
    # static(settings.STATIC_URL,documnet_root=settings.STATIC_ROOT)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,documnet_root=settings.STATIC_ROOT)
