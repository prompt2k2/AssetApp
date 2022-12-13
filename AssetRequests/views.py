from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Engineer, Site, UserProfile, AssetRequest
from .forms import SiteForm, RequestForm


def index(request):
    #r_form = SiteForm()
    r_site = Site.objects.all().order_by('name')
    # , 'r_form': r_form
    return render(request, 'index.html', {'r_site': r_site})


def UserProfile(request):
    return render(request, 'profile.html')


def MakeRequestView(request, id=0):
    if request.method == 'POST':
        if id == 0:
            siteform = SiteForm(request.POST)
            requestform = RequestForm(request.Post)
        else:

            site = Site.objects.get(id=id)
            siteform = SiteForm(request.POST, instance=site)
            requestform = RequestForm(request.POST)

        if siteform.is_valid() and requestform.is_valid():

            requestform.save()
            return redirect('/')

    else:

        if id == 0:
            siteform = SiteForm()
            requestform = RequestForm()
        else:
            site = Site.objects.get(id=id)
            siteform = SiteForm(instance=site)
            requestform = RequestForm()
    return render(request, 'assetrequest.html', {'siteform': siteform, 'requestform': requestform})


def ManagerAllocation(request, pk):
    manager = UserProfile.objects.get(id=pk)
    schedules = AssetRequest.objects.get(id=pk)
    request = []

    for schedule in schedules:
        if schedule.manager == manager:
            request.append(schedule.site)

    context = {'manager': manager, 'request': request}

    return render(request, 'manager_pending_list.html', {'mpl': context})


def pending_request(request):
    req = AssetRequest.objects.all_pending_requests()
    return render(request, 'pending_list.html', {'pending_list': req})
