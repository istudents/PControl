from django.db import models

# Create your models here.

class Traindetails(models.Model):
    train_no = models.IntegerField(max_length=5)
    #author = models.ForeignKey('Platform', on_delete=models.SET_NULL, null=True)
    train_name = models.CharField(max_length=30)
    train_dep = models.TimeField(blank=True, null=True)
    train_arr = models.TimeField(blank=True, null=True)
    train_source = models.CharField(max_length=20,blank=True)
    train_destination = models.CharField(max_length=20,blank=True)
    e_train_dep = models.TimeField(blank=True, null=True)
    e_train_arr = models.TimeField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null= True)

    class Meta:
        ordering = ['train_name']

    def __str__(self):
        return self.train_name

class Platform(models.Model):
    platformno = models.IntegerField(max_length=2,
    primary_key=True,)
    traindetails = models.OneToOneField(Traindetails,
    on_delete=models.CASCADE,)
    def __str__(self):
        return str(self.platformno)

    class Meta:
        ordering = ['platformno']

class Coachdetails(models.Model):
    coachname = models.CharField(max_length=10)

    class Meta:
        ordering = ['coachname']
    def __str__(self):
        return str(self.coachname)

class Trainlineup(models.Model):
    lineup = models.IntegerField(max_length=10)
    coachdet = models.OneToOneField(Coachdetails,
        on_delete=models.CASCADE,
        primary_key=True,)

    class Meta:
        ordering = ['lineup']
    def __str__(self):
        return str(self.coachdet)
