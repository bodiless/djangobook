from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import datetime
def hello(request):
	return HttpResponse("Hello World!")

def index(request):
	tmplt = get_template('base.html')
	now = get_datetime()
	html = tmplt.render(Context({'title': 'asdf', 'current_date': now}))
	return HttpResponse(html)

def one_hour_ahead(request,offset):
	try:		
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now()
	hour_ahead = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "Now is: %s <br/> In %s hours ahead will be: %s" % (now,offset,hour_ahead)
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	tmplt = get_template('datetime.html')
	html = tmplt.render(Context({'current_date': now}))
	return HttpResponse(html)

def get_datetime():
	now = datetime.datetime.now()
	return now

def for_loop(request):
	item_list = ("VM", "Honda", "Opel")
	tmplt = get_template('for.html')
	html = tmplt.render(Context({'item_list': item_list}))
	return HttpResponse(html)

def if_cond(request):
	var = ""
	tmplt = get_template('if_cond.html')
	html = tmplt.render(Context({'test': var}))
	return HttpResponse(html)

def if_equal(request):
	var = "test"
	tmplt = get_template('if_equal.html')
	html = tmplt.render(Context({'check': var}))
	return HttpResponse(html)

