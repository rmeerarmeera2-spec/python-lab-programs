from django.conf import settings
settings.configure(DEBUG=True,SECRET_KEY="123",
ROOT_URLCONF=__name__,ALLOWED_HOSTS=["*"],MIDDLEWARE=[])

import django
django.setup()
from django.http import HttpResponse
from django.urls import path

employees=[]

def home(request):
    h="""<h1>Employee Records</h1>
    <form method="post" action="/add/">
    Name: <input name="name">
    Department: <input name="dept">
    <button>Add</button></form><hr>"""
    for e in employees:
        h+=f"<p>{e['name']} - {e['dept']}</p>"
    return HttpResponse(h)

def add(request):
    if request.method=="POST":
        employees.append({"name":request.POST["name"],
                          "dept":request.POST["dept"]})
    return home(request)

urlpatterns=[path("",home),path("add/",add)]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py","runserver","0.0.0.0:8007"])