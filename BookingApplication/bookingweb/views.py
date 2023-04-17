from django.shortcuts import render,redirect
from django.views.generic import View

# Create your views here.

class IndexView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")