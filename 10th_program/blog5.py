from django.conf import settings
settings.configure(DEBUG=True,SECRET_KEY="123",
ROOT_URLCONF=__name__,ALLOWED_HOSTS=["*"],MIDDLEWARE=[])

import django
django.setup()
from django.http import HttpResponse
from django.urls import path

products=[]

def home(request):
    h="""<h1>Product Management</h1>
    <form method="post" action="/add/">
    Product: <input name="name">
    Price: <input name="price">
    <button>Add</button></form><hr>"""
    for p in products:
        h+=f"<p>{p['name']} - ₹{p['price']}</p>"
    return HttpResponse(h)

def add(request):
    if request.method=="POST":
        products.append({"name":request.POST["name"],
                         "price":request.POST["price"]})
    return home(request)

urlpatterns=[path("",home),path("add/",add)]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py","runserver","0.0.0.0:8009"])