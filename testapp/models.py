from django.db import models

# Create your models here.
class agent(models.Model):
    agentid=models.CharField(max_length=30)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    experience=models.CharField(max_length=5)
    company=models.CharField(max_length=10)
    def __str__(self):
        return self.firstname

class contact_info(models.Model):
    contactid=models.CharField(max_length=10)
    agentid= models.OneToOneField(agent,on_delete=models.CASCADE,primary_key=True)
    mobileno=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    def __str__(self):
        return self.contactid
class location(models.Model):

    locationid=models.CharField(max_length=30)
    agentloc=models.ForeignKey(agent,on_delete=models.CASCADE)
    locname=models.CharField(max_length=40)
    loccity=models.CharField(max_length=10)
    locstate=models.CharField(max_length=40)
    pincode=models.IntegerField(default=False)
    def __str__(self):
        return self.locname
class address (models.Model):
    #agentaddress = models.ForeignKey(agent,on_delete=models.CASCADE        )
    addressid=models.CharField(primary_key=True,max_length=100)
    agentid=models.ForeignKey(agent, on_delete=models.CASCADE )
    addressline1=models.CharField(max_length=100)
    addressline2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField(default=False)
    landmark=models.CharField(max_length=100)
    def __str__(self):
        return self.city
class reg(models.Model):
    user=models.CharField(max_length=10)
    pwd=models.CharField(max_length=10)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    dob=models.DateField()
    mob=models.IntegerField()
