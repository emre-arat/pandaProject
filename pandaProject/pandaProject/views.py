from django.shortcuts import render,redirect,HttpResponse


def base(request):
    return render(request,"base.html")
    