from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Engineer, Site, UserProfile, AssetRequest
from .forms import SiteForm, RequestForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect


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

            subject = ('Request for new Assets')
            manager = request.POST.get('site_manager')

            for e in User.objects.filter(id=manager):
                manager_email = e.email

            body = {}
            fullmessage = 'Dear Sir, \n\
                A request for new asset is awaiting your review and approval. \n\
                Please click here to access request and make necessary approval. \n\
                Thank you.'

            try:
                send_mail(
                    subject, fullmessage, settings.EMAIL_HOST_USER, [manager_email], fail_silently=False)

            except BadHeaderError:
                return HttpResponse("invalid Header Found")
            return print('Request Successful')  # redirect('/')

        # else:
        #     print(requestform.errors)

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


def approved_list(request):
    asset_req = AssetRequest.objects.all_approved_requests()
    return render(request, 'approved_list.html', {'approved_list': asset_req})


def approved_request(request):
    req = AssetRequest.objects.all_approved_requests()
    return render(request, 'approved_list.html', {'approved_list': req})


def RequestView(request, id):
    asset_req = get_object_or_404(AssetRequest, id=id)
    thesite = Site.objects.filter(name=asset_req.site)[0]

    return render(request, 'request_detail_view.html', {'asset_req': asset_req, 'site': thesite})


def approve_request(request, id):
    req = get_object_or_404(AssetRequest, id=id)
    place = req.site
    thesite = Site.objects.filter(name=place)[0]
    req.approve_request

    if req.approve_request:  # If manager approves the request
        subject = 'New Asset Request awaiting Approval',
        fullmessage = 'A new request for Asset on site is awaiting final approval',

        try:
            send_mail(
                # change this email to CTO email.
                subject, fullmessage, settings.EMAIL_HOST_USER, ['eebewele@starsightenergy.com'], fail_silently=False
            )
        except BadHeaderError:
            return HttpResponse("Invalid Header Found")
    return redirect('PendingRequest')


def reject_request(request,id):
    #context = dict()
    req = get_object_or_404(AssetRequest, id=id)
    place = req.site
    thesite = Site.objects.filter(name = place)[0]
    req.reject_request
    req.delete()
    #put a rejection message here to confirm reject 
    messages.error(request, 'Diesel request rejected for {0}'.format(thesite.name),extra_tags={"Reject"})
    return redirect('pending_requestlist')

###################################################################CTO APPROVAL#####################################################################################
j = 0


def cto_pending_list(request):
    req = AssetRequest.objects.cto_all_pending_requests()
    i = req.count()
    global j
    if i > j:
        subject = 'New Request for Asset Approval'
        fullmessage = 'Dear Sir, \n\
            A request for diesel is awaiting your review and approval. \n\
            Please click here to access request and approval. \n\
            Thank you.'
        try:
            send_mail(
                subject, fullmessage, settings.EMAIL_HOST_USER, [
                    'eebewele@starsightenergy.com'],  # change this to CTO email address
                fail_silently=False
            )
            j -= 1

        except BadHeaderError:
            return HttpResponse("Invalid Header Found")

    return render(request, 'cto_pending_list.html', {'cto_pending_list': req, 'title': 'Asset Request List - Pending Approval'})


def cto_approved_list(request):
    req = AssetRequest.objects.cto_all_approved_requests()
    return render(request, 'cto_approved_list.html', {'cto_approved_list': req, 'title': 'Asset Approval List - Approved'})


def cto_approve_request(request, id):
    req = get_object_or_404(AssetRequest, id=id)
    place = req.site
    thesite = Site.objects.filter(name=place)[0]
    req.cto_approve_request
    return redirect('CTOPendingRequest')


def cto_request_view(request, id):

    req = get_object_or_404(AssetRequest, id=id)
    thesite = Site.objects.filter(name=req.site)[0]  # topup_request.site

    return render(request, 'cto_request_detail_view.html', {'request_list': req})


def cto_reject_request(request, id):
    req = get_object_or_404(AssetRequest, id=id)
    place = req.site
    thesite = Site.objects.filter(name=place)[0]
    req.reject_request
    req.delete()
    messages.error(request, 'Asset Request rejected for {0}'.format(
        thesite.name), extra_tags={'Reject'})
    return redirect('CTOPendingRequest')


def cto_approval_form_view(request, id):
    return render(request, 'cto_approval.html')
###################################################################CTO APPROVAL#####################################################################################
