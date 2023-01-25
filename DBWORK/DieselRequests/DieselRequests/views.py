from django.shortcuts import render
from .models import showrecs, DeiselReport, Site, SiteReport


def showdata(request):
    r0 = DeiselReport.objects.all()
    r1 = Site.objects.all()
    r2 = SiteReport.objects.all()
    return render(request, "requests.html", {'r0':r0, 'r1':r1, 'r2':r2})