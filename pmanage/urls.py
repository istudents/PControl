from django.urls import path, re_path
from . import views

urlpatterns = [
    # Examples:
    path('', views.plathome, name='menupage'),
    #re_path(r'^$', views.homedisplay,name='homedisplay'),
    re_path(r'^pmangage/pno/(\d{1})/$',views.menupage4, name='menupage'),
    re_path(r'^pmangage/pno/(\d{2})/$',views.menupage4, name='menupage'),
    #re_path(r'^pc/pno/(\w\w)/$',views.menupage4, name='menupage'),
    re_path(r'^pmangage/traindetails/(\d{5})/$' ,views.menupage3, name='menupage'),
    # re_path(r'^blog/', include('blog.urls')),
    #re_path(r'^admin/', admin.site.urls),
]
