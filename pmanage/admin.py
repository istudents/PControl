from django.contrib import admin
from pmanage.models import Traindetails, Platform, Coachdetails, Trainlineup
from pmanage.homemodels import Menu, Footer, SiteInfo

# Register your models here.

admin.site.register(Traindetails)
admin.site.register(Platform)
admin.site.register(Coachdetails)
admin.site.register(Trainlineup)
admin.site.register(Menu)
admin.site.register(Footer)
admin.site.register(SiteInfo)
