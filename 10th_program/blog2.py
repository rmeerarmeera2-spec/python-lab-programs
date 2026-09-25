from django.conf import settings
settings.configure(DEBUG=True,SECRET_KEY="123",
ROOT_URLCONF=__name__,ALLOWED_HOSTS=["*"],MIDDLEWARE=[])

import django
django.setup()
from django.http import HttpResponse
from django.urls import path

events=[]

def home(request):
    h="""<h1>Event Management</h1>
    <form method="post" action="/add/">
    Event: <input name="event">
    Date: <input name="date">
    <button>Add</button></form><hr>"""
    for e in events:
        h+=f"<p>{e['event']} - {e['date']}</p>"
    return HttpResponse(h)

def add(request):
    if request.method=="POST":
        events.append({"event":request.POST["event"],
                       "date":request.POST["date"]})
    return home(request)

urlpatterns=[path("",home),path("add/",add)]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py","runserver","0.0.0.0:8006"])