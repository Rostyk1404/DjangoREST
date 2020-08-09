from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from csvparser.views import profile_upload

urlpatterns = [
    path('upload-csv/', profile_upload, name="profile_upload"),
]