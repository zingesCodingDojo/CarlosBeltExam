from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Travel, MultiUserTravel
from ..LoginRegistrationApp.models import User


def index(request):

    # If no cookie is saved of the user logging in, please redirect to home page.
    if "logged_user" in request.session:
        pass
    else:
        return redirect(reverse("splashpage:index"))
    context = {
        "current_user": Travel.objects.filter(user__pk=request.session["full_user"]),
        "all_users": Travel.objects.all().exclude(user__pk=request.session["full_user"]).exclude(travel_deetz__user__name=request.session["logged_user"]),
        "multitravelers": MultiUserTravel.objects.filter(user__name=request.session["logged_user"])

    }

    return render(request, "TravelerApp/index.html", context)


def logout(request):
    if request.method == "POST":
        del request.session["logged_user"]
    return redirect(reverse("splashpage:index"))


def new_trip(request):
    if "logged_user" in request.session:
        pass
    else:
        return redirect(reverse("splashpage:index"))
    context = {
        "current_user": request.session["full_user"]
    }

    return render(request, "TravelerApp/NewTrip.html", context)


def add_new_trip(request):
    if "logged_user" in request.session:
        pass
    else:
        return redirect(reverse("splashpage:index"))

    if request.method == "POST":

        response_from_models = Travel.objects.date_validation(request.POST, request.session["full_user"])

        if response_from_models["status"]:
            print("Trip made")
            new_stuff = response_from_models["new_trip"]
            print(new_stuff)
        else:
            for errors in response_from_models["errors"]:
                messages.error(request, errors)
                return redirect("/traveler/new_trip")

    return redirect("/")


def destinations(request, id):
    if "logged_user" in request.session:
        pass
    else:
        return redirect(reverse("splashpage:index"))

    context = {
        "current_stuff": Travel.objects.get(id=id),
        "multitravel": MultiUserTravel.objects.filter(travel=id),
        "logged_user": User.objects.get(id=int(request.session["full_user"]))
    }
    return render(request, "TravelerApp/TripDeetz.html", context)


def join(request, id):
    gimme_user = MultiUserTravel.objects.add_travelers(request.session["full_user"], id)

    return redirect("/")


def delete(request, id):
    Travel.objects.get(id=id).delete()
    return redirect("/")