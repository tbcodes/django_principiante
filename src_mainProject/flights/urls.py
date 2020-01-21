from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # creando diferentes Routes
    path("<int:flight_id>", views.flight, name="flight")
]