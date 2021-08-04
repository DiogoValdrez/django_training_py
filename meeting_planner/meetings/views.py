from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelform_factory

from .models import Meeting, Room
# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)#pk -> pri... key------get object or give error
    return render(request, "meetings/detail.html", {"meeting":meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form":form})