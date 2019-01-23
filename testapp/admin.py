from django.contrib import admin
from testapp.models import agent,contact_info,location,address,reg


# Register your models here.
class agentadmin(admin.ModelAdmin):
    list_display=['id','agentid','firstname','lastname','experience','company']
class agentadmininfo(admin.ModelAdmin):
    list_display=['contactid','agentid','mobileno','email']
class agentlocation(admin.ModelAdmin):
    list_display=['locationid','agentloc','loccity','locstate','pincode']
class agentadrs(admin.ModelAdmin):
    list_display=['addressid','agentid','addressline1','addressline2','city','state','pincode','landmark']
class agnreg(admin.ModelAdmin):
    list_display=['user','pwd','fname','lname','dob','mob']
admin.site.register(agent,agentadmin)
admin.site.register(contact_info,agentadmininfo)
admin.site.register(location,agentlocation)
admin.site.register(address,agentadrs)
admin.site.register(reg,agnreg)
