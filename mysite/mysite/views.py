from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello World!")

def whatANight(request):
	return HttpResponse("send me photo")

def finalyy