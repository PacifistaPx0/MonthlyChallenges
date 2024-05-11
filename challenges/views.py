from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
month_dict = {
    "january": "This is January",
    "february": "This is February",
    "march": "This is March",
    "april": "This is April",
    "may": "This is May",
    "june": "This is June",
    "july": "This is July",
    "august": "This is August",
    "september": "This is September",
    "october": "This is October",
    "november": "This is November",
    "december": "This is December"
}

def monthly_challenge_by_number(request, month):

    try:
        if month==0:
            return HttpResponseNotFound("Month does not exist")
        return HttpResponseRedirect("/challenges/" + list(month_dict.keys())[month-1])
    except:
        return HttpResponseNotFound("Month does not exist")


def monthly_challenge(request, month):
    try:
        challenge_text = month_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month does not exist")
    

