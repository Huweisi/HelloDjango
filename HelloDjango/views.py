from django.http import HttpResponse
def sayHello(request):
    return HttpResponse("Hello Django5!")