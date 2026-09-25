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

tasks = []

def home(request):
    html = """
    <h1>To-Do List</h1>

    <form method="post" action="/add/">
        Task: <input name="task">
        <button>Add Task</button>
    </form>

    <h2>Tasks</h2>
    """

    for i, task in enumerate(tasks):
        html += f"""
        <p>
        {task}
        <a href="/delete/{i}/">Delete</a>
        </p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        tasks.append(request.POST.get("task"))
    return home(request)

def delete(request, id):
    tasks.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py", "runserver", "0.0.0.0:8002"
])