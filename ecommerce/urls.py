from django.urls import path
from .views import home, catalogo, detalle, contacto

urlpatterns = [
    path("", home, name="home"),
    path("catalogo", catalogo, name="catalogo"),
    path("<int:key>", detalle, name="detalle"),
    path("contacto", contacto, name="contacto"),
]