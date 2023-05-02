from django.shortcuts import render

# Create your views here.
def web(request):
    return render(request,'webapp/webapp.html')
def pg_1(request):
    return render(request,'webapp/page-1.html')
def pg_2(request):
    return render(request,'webapp/page-2.html')
def pg_3(request):
    return render(request,'webapp/page-3.html')
def pg_4(request):
    return render(request,'webapp/page-4.html')
def pg_5(request):
    return render(request,'webapp/page-5.html')