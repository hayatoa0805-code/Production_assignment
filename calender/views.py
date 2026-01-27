from django.shortcuts import render,redirect
import calendar
from datetime import date
from events.models import Event

# Create your views here.
def calendar_view(request, year=None, month=None):
    if year is None or month is None:
        today = date.today()
        year = today.year
        month = today.month

    cal = calendar.monthcalendar(year, month)

    events = Event.objects.filter(
        date__year = year,
        date__month = month
    )

    events_by_day = {}

    for event in events:
        day = event.date.day
        if day not in events_by_day:
            events_by_day[day] = []
        events_by_day[day].append(event)

    context = {
        "year": year,
        "month": month,
        "cal": cal,
        "events_by_day":events_by_day,
    }

    return render(
        request,
        "calender/calendar_home.html",
        {
            "context":context
            }
        )


def month_minus_view(request, year, month):
    month -= 1
    if month == 0:
        month = 12
        year -= 1

    return redirect("calender:calendar_home", year=year, month=month)

def month_plus_view(request, year, month):
    month += 1
    if month == 13:
        month = 1
        year += 1

    return redirect("calender:calendar_home", year=year, month=month)