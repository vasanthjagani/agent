from django.shortcuts import render
from testapp.models import agent,location,contact_info,address,reg
from django.http import HttpResponse
from testapp.forms import regform,loginform

# Create your views here.
def agent1(request):
    agentrecords=agent.objects.all()
    return render(request,'testapp.html',{'agentrecord':agentrecords})
def agent2(request):
    agentrecords1=contact_info.objects.all()
    return render(request,'teatapp1.html',{'agentrecord1':agentrecords1})
def agent3(request):
    agentrecords2=location.objects.all()
    return render(request,'testapp2.html',{'agentrecord2':agentrecords2})
def agent4(request):
    agentrecords3=address.objects.all()
    return render(request,'testapp3.html',{'agentrecord3':agentrecords3})
def agent5(request):
    agentrecords4=address.objects.all()
    return render(request,'agent.html')
def form(request):
    return render(request,'form1.html')
def form1(request):
    try:
        Agentid=request.GET['agentid']
        First_name=request.GET['firstname']
        Lastname=request.GET['lastname']
        Experience=request.GET['experience']
        Company_name=request.GET['company']
        p1=agent(agentid=Agentid,firstname=First_name,lastname=Lastname,experience=Experience,company=Company_name)
        p1.save()
        return HttpResponse("<h1>agent data inserted succefully </h1>")
    except Exception as a:
        return HttpResponse(a)
def form2(request):
    return render(request,'form2.html')
def form3(request):
    try:
        Contact_id=request.GET['contactid']
        agent1=str(request.GET['agentid'])
        Agentid=agent.objects.get(agentid=agent1)
        mobile_no=request.GET['mobileno']
        Email=request.GET['email']
        contact_info(contactid=Contact_id,agentid=Agentid,mobileno=mobile_no,email=Email).save()
        return HttpResponse("<h1> contacts data inserted succefully </h1>")
    except Exception as e:
        return HttpResponse(e)

def form4(request):
    return render(request,'form3.html')
def form5(request):
    try:
        LOCATION_ID=request.GET['locationid']
        Agent2=str(request.GET['agentloc'])
        AGENT=agent.objects.get(agentid=Agent2)
        LOC_NAME=request.GET['locname']
        LOC_CITY=request.GET['loccity']
        LOC_STATE=request.GET['locstate']
        PINCODE=int(request.GET['pincode'])
        l1=location(locationid=LOCATION_ID,agentloc=AGENT,locname=LOC_NAME,loccity=LOC_CITY,locstate=LOC_STATE,pincode=PINCODE)
        l1.save()
        return HttpResponse("<h1> location data inserted succefully </h1>")
    except Exception as e :
        return HttpResponse(e)
def form6(request):
    return render(request,'form4.html')
def form7(request):
    try:
        Addressid=request.GET['addressid']
        Agent3=str(request.GET['agentid'])
        Agentid=agent.objects.get(agentid=Agent3)
        Addressline1=request.GET['addressline1']
        Addressline2=request.GET['addressline2']
        City=request.GET['city']
        State=request.GET['state']
        Pincode=request.GET['pincode']
        Landmark=request.GET['landmark']
        a1=address(addressid=Addressid,agentid=Agentid,addressline1=Addressline1,addressline2=Addressline2,city=City,state=State,pincode=Pincode,landmark=Landmark)
        a1.save()
        return HttpResponse("<h1> Address data inserted succefully </h1>")
    except Exception as ad:
        return HttpResponse(ad)
def record1(request):
    r1=agent.objects.filter(agentid='007')
    return render (request,'records.html',{'records':r1})
def record2(request):
    r2=contact_info.objects.filter(agentid=agent.objects.get(agentid='007'))
    print(r2)
    return render (request,'records2.html',{'records2':r2})
def record3(request):
    r3=location.objects.filter(agentloc=agent.objects.get(agentid='007'))
    print(r3)
    return render (request,'records3.html',{'records3':r3})
def record4(request):
    r4=address.objects.filter(agentid=agent.objects.get(agentid='007'))
    print(r4)

    return render (request,'records4.html',{'records4':r4})
def regs (request):
    return render(request,"reg.html")
def reg (request):
    if request.method=="post":
        forms=regform(request.post)
        if forms.is_valid():
            forms.save(commit=True)
            return HttpResponse("registation success")
        else:
            return HttpResponse("error")
    else:
        form=regform()
        return render (request,'reg1.html',{'form':form})
def login(request):
    if request.method=="post":
         myloginform=loginform(request.post)
         if myloginform.is_valid():
             un=myloginform.cleaned_data['user']
             pw=myloginform.cleaned_data['pwd']
             dbuser=reg.objects.filter(user=un,pwd=pw)
             if not dbuser:
                 return HttpResponse("login faild")
             else:
                return HttpResponse("login sucess")
    else:
        form=loginform()
        return render(request,'login.html',{'form':form})
