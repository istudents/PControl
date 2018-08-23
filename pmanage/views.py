from django.shortcuts import render
from django.http import HttpResponse
from pmanage.models import Traindetails, Platform, Trainlineup
from pmanage.homemodels import Menu, Footer, SiteInfo
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the pmanage index.")

def indexss(request):
    return HttpResponse("Hellosss, world. You're at the polls index.")

def plathome(request):
    footers = Footer.objects.all()
    siteinfos = SiteInfo.objects.filter(sitename__startswith = 'Pi')
    traindetails = Traindetails.objects.all()
    platforms = Platform.objects.all()
    return render(request,'pmanage/pmanage.html',{'footer':footers,'siteinfo':siteinfos,'traindetail':traindetails,'platform':platforms})

def menupage3(request, trainNo):
    footers = Footer.objects.all()
    siteinfos = SiteInfo.objects.filter(sitename__startswith = 'P')
    traindetails = Traindetails.objects.filter(train_no = trainNo)
    return render(request,'pmanage/picontroltest.html',{'footer':footers,'siteinfo':siteinfos, 'traindetail':traindetails})

def menupage4(request, abc):
    footers = Footer.objects.all()
    siteinfos = SiteInfo.objects.filter(sitename__startswith = 'P')
    traindets = Trainlineup.objects.all()
    return render(request,'pmanage/platcontrol.html',{'footer':footers,'siteinfo':siteinfos,'traindet':traindets})
