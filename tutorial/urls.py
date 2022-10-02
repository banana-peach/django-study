from django.urls import path, include

from tutorial.views import StudentView

urlpatterns = [
    path("new/", StudentView.as_view()),
]