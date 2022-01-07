#Create a proyect, create a new file called "views.py" inside of the folder, and inside put

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello world!')