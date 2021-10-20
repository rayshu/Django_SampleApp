from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Users

def index(request):
    users_list = Users.objects.order_by('name')
    users_list = list(users_list)
    context = {'users_list':users_list}
    return render(request,'covid_tracker_app/index.html', context )

def user(request, userid):
    user = get_object_or_404(Users, pk=userid)
    return render(request, 'covid_tracker_app/userDetails.html', {'user': user})

def register_user(request):
    if request.method == 'POST':
        form = Users(request.POST)
    else:
        form=Users()
    return render(request, 'covid_tracker_app/RegisterForm.html', {'form': form})