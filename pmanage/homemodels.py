from django.db import models

# Create your models here.

class Menu(models.Model):
    menuitem = models.CharField(max_length = 20)
    menuitemdesc = models.TextField()
    def __str__(self):
        return self.menuitem 

class Footer(models.Model):
    footeritems = models.CharField(max_length = 20)
    class Meta:
        ordering = ['footeritems']
    def __str__(self):
        return self.footeritems

class SiteInfo(models.Model):
    sitename = models.CharField(max_length = 20)
    siteinfo = models.TextField()
    def __str__(self):
        return self.sitename
