from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('airport.urls')),  # note singular 'airport/'
    path('', RedirectView.as_view(url='/airport/', permanent=False)),
    path('flights/', include('flights.urls', namespace='flights')),# flights 
    path('booking/', include('booking.urls')),
    
    path('',include('authentication.urls')),#authentications
    
    
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)