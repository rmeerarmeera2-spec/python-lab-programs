from django.conf import settings
settings.configure(DEBUG=True,SECRET_KEY="123",
ROOT_URLCONF=__name__,ALLOWED_HOSTS=["*"],MIDDLEWARE=[])

import django
django.setup()
from django.http import HttpResponse
from django.urls import path

patients=[]

def home(request):
    h="""<h1>Patient Management</h1>
    <form method="post" action="/add/">
    Name: <input name="name">
    Problem: <input name="problem">
    <button>Add</button></form><hr>"""
    for p in patients:
        h+=f"<p>{p['name']} - {p['problem']}</p>"
    return HttpResponse(h)

def add(request):
    if request.method=="POST":
        patients.append({"name":request.POST["name"],
                         "problem":request.POST["problem"]})
    return home(request)

urlpatterns=[path("",home),path("add/",add)]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py","runserver","0.0.0.0:8008"])