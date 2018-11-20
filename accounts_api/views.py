# from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User

from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from movies_api.models import Movie
from django.contrib import auth

import json

# Create your views here.

@ensure_csrf_cookie
def getToken(request):
	return JsonResponse({'data': 'Token Successful'}, safe=False)

def logout(request):
	print('request.user in logout: ', request.user)
	auth.logout(request)
	print('request.user.is_authenticated in logout: ', request.user.is_authenticated)
	return JsonResponse({'data': 'Logout Successful'}, safe=False)

class CreateUser(View):

	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			new_user = User(username=data['username'], password=data['password'], email=data['email'])
			new_user.set_password(new_user.password)
			new_user.save()
			auth.login(request, new_user)

			return JsonResponse({'data': 'Registration Successful'}, safe=False)

		except:
			return JsonResponse({'error': 'Registration Unsuccessful'}, safe=False)

class Authentication(View):

	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		user = auth.authenticate(username=data['username'], password=data['password'])
		if user is not None:
			auth.login(request, user)
			return JsonResponse({'data': 'Login Successful'}, safe=False)
		else:
			return JsonResponse({'data': 'Login Unsuccessful'}, safe=False)

class User_Detail(View):
	def get(self, request, pk):
		user = list(User.objects.filter(pk=pk).values())
		user_movies = list(Movies.objects.filter(created_by_id=pk).values())
		print('user_movies from User_Detail get request: ', user_movies)
		return JsonResponse({'data': {'user': user, 'movies': user_movies}}, safe=False)





