from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: HttpResponse("Hello World"), name="index"),
    path(
        "test_exists",
        lambda request: HttpResponse("Hello World", headers={'Permissions-Policy': 'geolocation=*, camera=()'})
    )
]
