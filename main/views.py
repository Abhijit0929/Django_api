from django.shortcuts import render
from django.http import JsonResponse
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SmartBin, Pickup, WasteReport
from .serializers import SmartBinSerializer, PickupSerializer, WasteReportSerializer



# Page view (HTML)
from rest_framework import viewsets
from .models import SmartBin
from .serializers import SmartBinSerializer



@api_view(['PATCH'])
def update_pickup_status(request, id):

    pickup = Pickup.objects.get(id=id)

    serializer = PickupSerializer(
        pickup,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def bin_list_create(request):

    if request.method == "GET":
        bins = SmartBin.objects.all()
        serializer = SmartBinSerializer(bins, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = SmartBinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['PATCH'])
def bin_update(request, id):

    bin = SmartBin.objects.get(id=id)

    serializer = SmartBinSerializer(
        bin,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET','POST'])
def pickup_list_create(request):

    if request.method == "GET":
        pickups = Pickup.objects.all()
        serializer = PickupSerializer(pickups, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PickupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
@api_view(['GET','POST'])
def report_list_create(request):

    if request.method == "GET":
        reports = WasteReport.objects.all()
        serializer = WasteReportSerializer(reports, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = WasteReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class SmartBinViewSet(viewsets.ModelViewSet):
    queryset = SmartBin.objects.all()
    serializer_class = SmartBinSerializer


from django.shortcuts import render, redirect
from .models import SmartBin, WasteReport


def home(request):

    return render(request,"home.html")


def bins_view(request):

    bins = SmartBin.objects.all()

    return render(request,"bins.html",{"bins":bins})


def report_waste(request):

    if request.method == "POST":

        location = request.POST.get("location")
        description = request.POST.get("description")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        WasteReport.objects.create(
            location=location,
            description=description,
            latitude=latitude,
            longitude=longitude,
            status="open",
            user=request.user
        )

        return redirect("/reports/")

    return render(request,"report.html")

def reports_view(request):

    reports = WasteReport.objects.all()

    return render(request,"reports.html",{"reports":reports})


# Pickups page view

from .models import Pickup

def pickups_view(request):

    pickups = Pickup.objects.all()

    return render(request, "pickups.html", {"pickups": pickups})



def update_pickup(request, id):

    pickup = Pickup.objects.get(id=id)

    if pickup.status == "pending":
        pickup.status = "in_progress"

    elif pickup.status == "in_progress":
        pickup.status = "completed"

    pickup.save()

    return redirect("/pickups/")

def city_dashboard(request):
    bins=SmartBin.objects.all()
    reports=WasteReport.objects.all()
    pickups=Pickup.objects.all()
    
    context={
        "bins":bins,
        "reports":reports,
        "pickups":pickups
    }
    
    return render(request,"dashboard.html",context)
    
    
from .models import SmartBin, Pickup, WasteReport
from django.contrib.auth.models import User
from django.shortcuts import render


def admin_dashboard(request):

    total_bins = SmartBin.objects.count()
    full_bins = SmartBin.objects.filter(status="full").count()
    pending_pickups = Pickup.objects.filter(status="pending").count()
    reports = WasteReport.objects.count()
    workers = User.objects.count()

    context = {
        "total_bins": total_bins,
        "full_bins": full_bins,
        "pending_pickups": pending_pickups,
        "reports": reports,
        "workers": workers
    }

    return render(request,"admin_dashboard.html",context)


from django.shortcuts import render
from .models import SmartBin

def admin_bins(request):

    bins = SmartBin.objects.all()

    return render(request,"admin_bins.html",{"bins":bins})

