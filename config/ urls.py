from django.urls import path, include

urlpatterns = [
    path("api/v1/user/", include("apps.user.urls.v1.urls")),
    # Add more versions or modules here
]
