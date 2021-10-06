from django.http import httpRequest

def index(request):
    return httpResponse('''Welcome to your first Django App''')

