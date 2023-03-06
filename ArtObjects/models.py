from django.db import models

# Create your models here.
# Models for Art Objects and Its data.


class Hall(models.Model):
    hall_name=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.hall_name
    

class ArtObject(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    epoch = models.CharField(max_length=255,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=1)
    last_modified = models.DateTimeField(auto_now=1)
    #images = still not added   
    active = models.BooleanField(default=True)
    hall = models.ForeignKey(Hall,on_delete=models.SET_DEFAULT, default='8')
    # 8 is Inventory
    
    def __str__(self) -> str:
        return self.name
    
class Description (models.Model):
    description = models.TextField(null=True,blank=True,default='None')
    art_object = models.OneToOneField('ArtObject', related_name='Description', on_delete=models.CASCADE, primary_key= True)
    #name = art_object.name 
    ## use the name for searching in Description table
    
    def __str__(self) -> str:
        return self.art_object.name
    
    
class ArtStory(models.Model):
    story = models.TextField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject,related_name='ArtStory',on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self) -> str:
        return self.art_object.name
    

class BorrowedCollection(models.Model):
    date_borrowed = models.DateTimeField(null=True,blank=True)
    date_returned = models.DateTimeField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,primary_key=True) 
    
    def __str__(self) -> str:
        return self.art_object.name
    

class PermenantCollection(models.Model):
    date_aquired = models.DateTimeField(null=True,blank=True)
    art_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self) -> str:
        return self.art_object.name

class Other(models.Model):
    origin = models.CharField(max_length=255,null=True,blank=True)
    art_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return self.art_object.name

class Chariot(models.Model):
    object_number = models.IntegerField(null=True,blank=True)
    origin = models.CharField(max_length=255,null=True,blank=True)
    chassis_number = models.CharField(max_length=255,null=True,blank=True)
    art_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return self.art_object.name


class Painting(models.Model):
    artist_name = models.CharField(max_length=255,null=True,blank=True)
    art_object = models.OneToOneField(ArtObject,on_delete=models.CASCADE,primary_key=True)

    #def __str__(self) -> str:
        #return self.art_object.name

class Holding(models.Model):
    material = models.CharField(max_length=255,null=True,blank=True)
    art_object = models.ForeignKey(ArtObject,on_delete=models.CASCADE)

    #def __str__(self) -> str:
        #return self.art_object.name