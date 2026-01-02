from django.urls import path
from .views import upload_view, history_view

urlpatterns = [
    path("", upload_view, name="upload"),
    path("history/", history_view, name="history"),
]
