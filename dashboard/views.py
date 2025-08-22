from django.shortcuts import render

def dashboard_home(request):

    return render(request, 'dashboard/dasboard_home.html')