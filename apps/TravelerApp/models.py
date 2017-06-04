from __future__ import unicode_literals
from django.db import models
from time import strftime
from ..LoginRegistrationApp.models import User


class TravelManager(models.Manager):
    def date_validation(self, postData, user_id):

        errors = []

        # Verify departure is higher than current time.
        if len(postData["destination"]) < 1:
            errors.append("Destination cannot be empty!")

        if postData["depart_at"][:4] >= strftime("%Y") and postData["depart_at"][5:7] >= strftime("%m") and \
                        postData["depart_at"][8:10] >= strftime("%d"):
            pass
        else:
            errors.append("Departure day must be past today's date!")

        # Verify return date is higher than departure date.
        if postData["depart_at"][:4] >= postData["return_date"][:4] and \
            postData["depart_at"][5:7] >= postData["return_date"][5:7] and \
            postData["depart_at"][8:10] >= postData["return_date"][8:10]:
            errors.append("Departure cannot be a date that is later than return date!")

        response_to_views = {}
        if len(errors):
            response_to_views["status"] = False
            response_to_views["errors"] = errors
        else:
            response_to_views["status"] = True
            new_trip = self.create(destination=postData["destination"], description=postData["description"],
                                   departure=postData["depart_at"], return_date=postData["return_date"],
                                   user=User.objects.get(id=user_id))
            response_to_views["new_trip"] = new_trip
        return response_to_views


class Travel(models.Model):
    destination = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    departure = models.DateTimeField()
    return_date = models.DateTimeField()
    user = models.ForeignKey(User, related_name="user_trip", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()


class MultiUserTravelManager(models.Manager):
    def add_travelers(self, user, travel_id):
        return self.create(user=User.objects.get(id=user), travel=Travel.objects.get(id=travel_id))


class MultiUserTravel(models.Model):
    user = models.ForeignKey(User, related_name="user_added_trip", on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, related_name="travel_deetz", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MultiUserTravelManager()
