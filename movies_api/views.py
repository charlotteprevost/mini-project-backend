# from django.shortcuts import render

from django.http import JsonResponse

from django.views import View
from .models import Movie
from django.contrib.auth.models import User

import json

# Create your views here.

class Movies(View):

	def get(self, request):
		if(request.user.is_authenticated):                  # is_authenticated is a built-in method to request
			user = User.objects.get(id=request.user.id)     
			movies_list = list(user.movies.all().values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'status': 200,
			'data': movies_list
			}, safe=False)


	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)

		print('Request: ', request)

		try:
			new_movie = Movie(title=data['title'], release_date=data['release_date'], synopsis=data['synopsis'])
			new_movie.created_by = request.user
			new_movie.save()
			data['id'] = new_movie.id

			print('data: ', data)

			return JsonResponse({'data': data}, safe=False)

		except:
			return JsonResponse({'error': 'Invalid data in post request'}, safe=False)


class Movie_detail(View):

	def get(self, request, pk):
		movie_list = list(Movie.objects.filter(pk=pk).values())
		return JsonResponse({'data': movie_list}, safe=False)

	def put(self, request, pk):
		data = request.body.decode('utf-8')
		data = json.loads(data)

		try:
			edit_movie = Movie.objects.get(pk=pk)
			data_key = list(data.keys())

			for key in data_key:
				if key == 'title':
					edit_movie.title = data[key]
				if key == 'release_date':
					edit_movie.release_date = data[key]
				if key == 'synopsis':
					edit_movie.synopsis = data[key]

			edit_movie.save()

			data['id'] = edit_movie.id

			return JsonResponse({'data': data}, safe=False)

		except Movie.DoesNotExist:
			return JsonResponse({'error': 'Your movie''s primary key doesn''t exist'}, safe=False)

		except:
			return JsonResponse({'error': 'Invalid Data'}, safe=False)


	def delete(self, request, pk):
		try:

			movie_to_delete = Movie.objects.get(pk=pk)
			movie_to_delete.delete()

			return JsonResponse({'data': True}, safe=False)
		except:
			return JsonResponse({'error': 'Invalid Data'}, true=False)



















