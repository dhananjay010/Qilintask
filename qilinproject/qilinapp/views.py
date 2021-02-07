from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from qilinapp.models import Restaurant
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def signUp(request):
	if request.method == "POST":
		request_body = json.loads(request.body.decode())
		user = User(request_body)
		password1 = request_body['password']
		password2 = request_body['confirm_password']
		username = request_body['username']
		last_name = request_body['last_name']
		first_name = request_body['first_name']
		email = request_body['email']
		if password1 == password2 :
			if User.objects.filter(username=username).exists():
				return JsonResponse({"response": "username taken."})
			elif User.objects.filter(email=email).exists():
				return JsonResponse({"response": "email taken."}) 
			else:
				user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
				user.save()
				return JsonResponse({"response": "user created."})
		else: 
			return JsonResponse({"message": "password is not matching."})
	else:
		JsonResponse({"message": "This method is invalid."})

@csrf_exempt
def signIn(request):
	if request.method == "POST":
		request_body = json.loads(request.body.decode())
		username = request_body['username']
		password = request_body['password']

		user = auth.authenticate(username = username, password = password)
		if user is not None:
			return JsonResponse({"message": "You've logged in successfully."})
		else:
			return JsonResponse({"message": "Please enter the correct username and password."})
		
	else:
		return JsonResponse({"message": "invalid method."})



def getFoodCategory(request,food_category):
	try:
		objects = Restaurant.objects.all().filter(foodCategory = food_category).values('foodCategory').distinct()
		return JsonResponse({"response": list(objects)})
	except:
		return JsonResponse({"response": []})

def getFoodItems(request,food_category):
	try:
		objects = Restaurant.objects.all().filter(foodCategory = food_category).values('foodItems').distinct()
		return JsonResponse({"response": list(objects)})
	except:
		return JsonResponse({"response": []})

def getFoodItemOnAttribute(request,food_attribute,food_category = None):
	try:
		if food_category == None:
			objects = Restaurant.objects.all().filter(foodAttribute = food_attribute).values('foodItems').distinct()
		else:
			objects = Restaurant.objects.all().filter(foodAttribute = food_attribute, foodCategory = food_category).values('foodItems').distinct()
			print(objects)
		return JsonResponse({"response": list(objects)})
	except:
		return JsonResponse({"response": []})


def getPrice(request,upper_limit,lower_limit):
	try:
		objects = Restaurant.objects.all().filter(price__lte = upper_limit, price__gte = lower_limit ).values('foodItems')
		return JsonResponse({"response": list(objects)})
	except:
		return JsonResponse({"response": []})

def search(request,search_object):
	try:
		food_items = Restaurant.objects.all().filter(foodItems__icontains=search_object).values()
		food_category = Restaurant.objects.all().filter(foodCategory__icontains=search_object).values()
		if len(food_category) > 0:
			return JsonResponse({"response": list(food_category)})
		elif len(food_items) > 0:
			return JsonResponse({"response": list(food_items)})
		else:
			return JsonResponse({"response": []})
	except:
		return JsonResponse({"response": []})