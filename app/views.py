from django.shortcuts import render

from app.froms import ImageForm
from app.models import Images


# Create your views here.
def home(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
    img=Images.objects.all()
    form=ImageForm()
    return render(request,'home.html',{'form':form,'img':img})
