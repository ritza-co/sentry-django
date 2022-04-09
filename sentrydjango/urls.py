from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def trigger_error(request):
    try:
        division_by_zero = 1 / 0
    except:
        division_by_zero = "Hello World"

    return HttpResponse(division_by_zero)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('names.urls')),
    path('sentry-debug/', trigger_error),
]
