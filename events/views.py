from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    # convert month to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create a calendar

    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')

    return render(request,
                  'events/home.html', {
                      "year": year,
                      "month": month,
                      "month_number": month_number,
                      "cal": cal,
                      "current_year": current_year,
                      "time": time,
                  })
