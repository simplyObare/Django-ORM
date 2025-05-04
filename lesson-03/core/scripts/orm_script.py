from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():

    # filter down to only Chinese restaurant
    print(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE))

    pprint(connection.queries)
