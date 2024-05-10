from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This is January"
    elif month == "february":
        challenge_text = "This is February"
    elif month == "march":
        challenge_text = "This is March"
    else:
        return HttpResponseNotFound("This month does not exist")
    return HttpResponse(challenge_text)
