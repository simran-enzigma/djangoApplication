from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
import operator
from django.db.models import Q

def home(request):
    result = Contact.objects.all()
    return render(request,'ContactManagerApp/contacts.html',{'ListOfContact':result})

def EditContact(request,SerialNo):
    if(request.method=='GET'):
        if (SerialNo==None):
            c_form = ContactForm()
        else:
            result = Contact.objects.filter(SerialNo=SerialNo)
            c_form = ContactForm(instance=result[0])
        return render(request,'ContactManagerApp/manage_contact.html',{'c_form':c_form})
    else:
        record=Contact()
        record.SerialNo = SerialNo
        record.FirstName = request.POST['FirstName']
        record.LastName=request.POST['LastName']
        record.Email=request.POST['Email']
        record.MobileNo=request.POST['MobileNo']
        record.save()
        result= Contact.objects.all()
        return render(request,'ContactManagerApp/contacts.html',{'ListOfContact':result})

def DeleteContact(request,SerialNo):
     if(request.method=='GET'):
        result = Contact()
        result.SerialNo = SerialNo
        result.delete()
        result= Contact.objects.all()
        return render(request,'ContactManagerApp/contacts.html',{'ListOfContact':result})
        
def AddContact(request):
    return EditContact(request,None)

def searchContact(request,search):
     if(request.method=='GET'):
         if(search==None):
             result = Contact()
             result = Contact.objects.all()
         else:
             result = Contact.objects.filter(FirstName__contains=search)
     return render(request,'ContactManagerApp/contacts.html',{'ListOfContact':result})