from django.conf.urls import url
from . import views

# Our user has logged in and is now viewing travel plans.
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^logout$", views.logout, name="logout"),
    url(r"^new_trip$", views.new_trip, name="new_trip"),
    url(r"^add_new_trip$", views.add_new_trip, name="add_new_trip"),
    url(r"^destinations/(?P<id>\d+)?", views.destinations, name="destinations"),
    url(r"^join/(?P<id>\d+)?", views.join, name="join_trip"),
    url(r"^delete/(?P<id>\d+)?", views.delete, name="delete")
]
