from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_view, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing'),
    path('leads/', include("leads.urls", namespace="leads")),
    # static(settings.STATIC_URL,documnet_root=settings.STATIC_ROOT)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,documnet_root=settings.STATIC_ROOT)
