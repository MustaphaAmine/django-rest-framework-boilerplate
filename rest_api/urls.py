from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path('app-subpath/', views.handling_request_view.as_view())
]