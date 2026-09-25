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
books = []
def home(request):
    html = """
    <h1>Library Management</h1>
    <form method="post" action="/add/">
        Book Name: <input name="book"><br><br>
        Author: <input name="author"><br><br>
        <button>Add Book</button>
    </form>
    <h2>Books</h2>
    """

    for i, b in enumerate(books):
        html += f"""
        <p>{b['book']} - {b['author']}
        <a href="/delete/{i}/">Delete</a></p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        books.append({
            "book": request.POST.get("book"),
            "author": request.POST.get("author")
        })
    return home(request)

def delete(request, id):
    books.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py", "runserver", "0.0.0.0:8001"
])