# from django.shortcuts import render

from django.http import JsonResponse

from django.views import View
# from .models import Movie
from django.contrib.auth.models import User

import requests
import json

# Create your views here.
import requests


# class SearchMovie(View):

	# url = "http://api-public.guidebox.com/v2/search"

	# payload = (
	# 	('api_key', '7eec0384545005656d8702d02413111dbd7d6f1b'),
	# 	('type', 'movie'),
	# 	('field', 'title'),
	# 	('query', 'Terminator')
	# )

	# headers = {
	# 	'Content-Type': "application/json;charset=utf-8",
	# 	# 'Authorization': "Bearer <<access_token>>"
	# 	}

	# response = requests.request("GET", url, params=payload, headers=headers)
	# print(response.text)
	


class Search_Result(View):

	def get(self, request, searchTerm):
		
		search = searchTerm
		url = "http://api-public.guidebox.com/v2/search"

		payload = (
			('api_key', '7eec0384545005656d8702d02413111dbd7d6f1b'),
			('type', 'movie'),
			('field', 'title'),
			('query', searchTerm)
		)

		headers = {
			'Content-Type': "application/json;charset=utf-8",
			# 'Authorization': "Bearer <<access_token>>"
			}

		response = requests.request("GET", url, params=payload, headers=headers)
		print(response.text)

		return JsonResponse({'data': response}, safe=False)











