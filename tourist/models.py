from django.db import models


from django.db import models



# Create your models here.


class Tourist(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    firstname = models.CharField(max_length=200, blank=True,null=True)
    lastname = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.firstname+""+self.lastname)
   

