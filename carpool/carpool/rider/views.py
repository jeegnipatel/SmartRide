from django.shortcuts import render
from django.http import HttpResponse ,Http404
from django.template import loader
from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import ride
import numpy as np
import googlemaps 
import json
import sqlite3
from django.core import serializers
import time


from django.http import JsonResponse


# Create your views here.

def index(request):
	print(request.user.username)
	return render(request , "riderHome.html" , {'username' : request.user.username})
	# return HttpResponse("<h1>SUCCESS</h1>")

def rideInfo(request):
	if request.method == "POST":
		print("ride info---------------------------------------------------------------------------------------")
		print(request.POST['userId'])
		print(request.POST['pickup'])
		print(request.POST['destination'])
		print(request.POST['latVal'])
		print(request.POST['lngVal']) 
		print(type(request.POST))
		r = ride(
			userId = request.POST['userId'], 
			pickUp = request.POST['pickup'],
			destination = request.POST['destination']
		)
		r.save()
		context ={'paramDict' : {'userId' : request.POST['userId'],'pickup' : request.POST['pickup'] , 'latVal' : request.POST['latVal'] , 
					'lngVal' : request.POST['lngVal'] , 'destination' : request.POST['destination'] }}
		#model of ride created
	return render(request , "blank.html" , context)

def statusUpdate(request):
	print("here ----------------------------------")
	id = request.GET['id']
	update =request.GET['update']
	gmaps = googlemaps.Client(key='AIzaSyCG-rWicPLs2VaZF3WDK6yyl7tQqh-kUUc')
	rideDetils = get_object_or_404(ride, pk=id)

	my_dist_1 = gmaps.distance_matrix(rideDetils.pickUp , rideDetils.destination)['rows'][0]['elements'][0]["distance"]["value"]
	time.sleep(10)

	my_dist_1 = gmaps.distance_matrix(rideDetils.pickUp, rideDetils.destination)['rows'][0]['elements'][0]["distance"][
		"value"]

	my_dist_1 = my_dist_1/1000.0
	my_dist_1 = int(my_dist_1 *10)
	print("hello ----------------------------------",id)
	if rideDetils.status :
		if rideDetils.complete:
			return JsonResponse({'success':True,'driverId':rideDetils.driverId,'complete':True,'cost':my_dist_1, 'expectedTime':rideDetils.expectedTime})
		else:
			return JsonResponse({'success':True,'driverId':rideDetils.driverId,'complete':False,'cost':my_dist_1, 'expectedTime':rideDetils.expectedTime})
	return JsonResponse({'success':False,'driverId':"none",'complete':False,'cost':0, 'expectedTime':rideDetils.expectedTime})

## UNCOMMENT - if we redirect to new page after ride acceptance
def rideSuccessful(request):
	print("kkk ----------------------------------")
	if request.method == "POST":
		id = request.POST['userId']
		print("rider id", id)
		rideDetails = get_object_or_404(ride, pk=id)
	#return render(request, 'polls/results.html', {'rideDetails': rideDetails})
	return HttpResponse("<h1>SUCCESS </h1>")

# def endRide(request):
# 	print(request.GET['id'], "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 	ride.objects.filter(pk=request.GET['id']).delete()
# 	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6")
# 	return render(request , "drive_or_ride.html" , {'user': request.GET['id']})

def riderQuestions(request):
    print(request.user.username)
    return render(request, "riderSideQuestion.html", {'username': request.user.username})


def riderAnswer(request):
    if request.method == "POST":
        userid = request.user.username
        riderid = userid
        talkative = request.POST.get('talkative')
        timedriving = request.POST.get('timedriving')
        music = request.POST.get('music')
        male = request.POST.get('male')
        female = request.POST.get('female')
        student = request.POST.get('student')
        working = request.POST.get('working')
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        values = (userid, riderid, talkative, timedriving, music, male, female, student, working)
        cur.execute("insert into rider_question values (?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
        con.commit()
        return render(request, "riderHome.html", {'username': request.user.username})