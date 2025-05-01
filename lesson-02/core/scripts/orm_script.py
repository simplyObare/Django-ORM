from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():

    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating = Rating(restaurant=restaurant, user=user, rating=9)

    rating.full_clean()
    rating.save()

    # pprint(connection.queries)
