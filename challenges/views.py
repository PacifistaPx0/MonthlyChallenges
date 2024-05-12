from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



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

# Create your views here.


def index(request):
    list_items = ""
    months = list(month_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{
            capitalized_month}</a></li>"

    # "<li><a href=""...">january</a><li><a href="...">february</a>...

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):

    try:
        if month == 0:
            return HttpResponseNotFound("Month does not exist")
        redirect_month = list(month_dict.keys())[month-1]
        redirect_path = reverse(
            "month-challenge", args=[redirect_month])  # /challenge/january
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Month does not exist")


def monthly_challenge(request, month):
    #try:
        challenge_text = month_dict[month]
        redirect_month = month.capitalize()
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": redirect_month
        })
    #except:
        #return HttpResponseNotFound("<h1>This month does not exist</h1>")
