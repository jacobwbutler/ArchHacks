from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from website.models import Doctor, Adherence, Target, Rx, Note, Case, Patient


# from django.core.context_processors import csrf

# Create your views here.
def index(request):
    return render(request, 'index.html')


def patient_profile(request):
    return render_to_response('patientprofile.html')


def login(request):
    return render_to_response('index.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        if user.has_perm('website.add_case'):
            return render(request, 'doctor.html')
        else:
            parent = Patient.objects.filter(first_name=user.first_name)
            case_list = [c.cases for c in Patient.objects.filter(first_name=user.first_name)]
            print(case_list)
            return render(request, 'patient.html', {'cases': case_list})
    else:
        return HttpResponseRedirect('invalid_login')


def loggedin(request):
    return render_to_response('loggedin.html', request.user.username)  # 'full_name': request.user.username)


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
