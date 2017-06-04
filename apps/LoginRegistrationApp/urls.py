from django.conf.urls import url
from . import views

# Index routes to our home page which is login registration
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^register$", views.register),
    url(r"^login$", views.login)

]
