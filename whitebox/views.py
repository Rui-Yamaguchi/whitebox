from django.shortcuts import render

def WhiteboxView(request):
    return render(request, 'whitebox/WHITEBOX.html')

def Howaito(request):
    return render(request, 'whitebox/howaito.html')

def Rio(request):
    return render(request, 'whitebox/rio.html')

def Aka(request):
    return render(request, 'whitebox/aka.html')

def Tedhi(request):
    return render(request, 'whitebox/teddy.html')

def Coco(request):
    return render(request, 'whitebox/coco.html')

def Wiru(request):
    return render(request, 'whitebox/will.html')

def Communication(request):
    return render(request, 'whitebox/communication.html')