from django.db import models

# Create your models here.

class Museum_Info(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    contact_mail = models.EmailField(null=True,blank=True)
    contact_phone = models.CharField(max_length=255,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    halls_number = models.PositiveSmallIntegerField(null=True,blank=True)
    
    #def __str__(self) -> str:
        #return self.name
    
class Openning_Hour(models.Model):
    day_choices = [
        ('FR','Friday'),
        ('ST','Saturday'),
        ('SN','Sunday'),
        ('MN','Monday'),
        ('TU','Tuseday'),
        ('WE','Wednesday'),
        ('TH','Thursday'),
    ]
    day = models.CharField(max_length=2, choices = day_choices,null=True,blank=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    museum_info = models.OneToOneField('Museum_Info',related_name= 'openning_Hours', on_delete=models.CASCADE, primary_key= True)

    #def __str__(self) -> str:
       # return self.day

class Event(models.Model): 
    name = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_about = models.TextField(null=True,blank=True)
    museum_info = models.ForeignKey('Museum_Info',related_name= 'Events', on_delete=models.CASCADE)

    #def __str__(self) -> str:
        #return self.name
    
class Media(models.Model):
    media = models.ImageField(verbose_name=('Imagefile'), blank= True)
    name = models.CharField(max_length=255, blank= True,null = True)

    museum_info = models.ForeignKey('Museum_Info', on_delete=models.CASCADE)
    
class User(models.Model):
     museum_info = models.ForeignKey('Museum_Info', on_delete=models.PROTECT)
     name = models.CharField(max_length=255,null=True,blank=True)

     #def __str__(self) -> str:
       # return self.name