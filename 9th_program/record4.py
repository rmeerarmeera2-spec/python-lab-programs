from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

contacts = []

def home(request):
    html = """
    <h1>Contact Management</h1>

    <form method="post" action="/add/">
        Name: <input name="name"><br><br>
        Phone: <input name="phone"><br><br>
        Email: <input name="email"><br><br>
        <button>Add Contact</button>
    </form>

    <h2>Contact List</h2>
    """

    for c in contacts:
        html += f"""
        <p>
        {c['name']} - {c['phone']} - {c['email']}
        </p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        contacts.append({
            "name": request.POST.get("name"),
            "phone": request.POST.get("phone"),
            "email": request.POST.get("email")
        })
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add)
]

from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py", "runserver", "0.0.0.0:8003"
])