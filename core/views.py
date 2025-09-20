from django.http import HttpResponse

def home (request):
    return HttpResponse("<h1>Oi mundo, django aqui</h1>")