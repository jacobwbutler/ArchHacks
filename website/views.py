from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

#from django.core.context_processors import csrf

# Create your views here.
def index(request):
	return render(request, 'patient.html')

def login(request):
	#c = {}
	#c.update(csrf(request))
	return render_to_response('login.html')#, c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		if user.has_perm('website.add_case') :
			return render(request, 'doctor.html')
		else:
			return render(request, 'patient.html')
	else:
		return HttpResponseRedirect('invalid_login')

def loggedin(request):
	return render_to_response('loggedin.html', request.user.username)#'full_name': request.user.username)

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')