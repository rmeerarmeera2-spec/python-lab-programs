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

employees = []

def home(request):
    html = """
    <h1>Employee Management</h1>

    <form method="post" action="/add/">
        Name: <input name="name"><br><br>
        Department: <input name="dept"><br><br>
        Salary: <input name="salary"><br><br>
        <button>Add Employee</button>
    </form>

    <h2>Employee List</h2>
    """

    for e in employees:
        html += f"""
        <p>
        Name: {e['name']} |
        Department: {e['dept']} |
        Salary: {e['salary']}
        </p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        employees.append({
            "name": request.POST.get("name"),
            "dept": request.POST.get("dept"),
            "salary": request.POST.get("salary")
        })
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add)
]

from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py", "runserver", "0.0.0.0:8004"
])