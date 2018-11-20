from django.urls import path
from .views import Search_Result
# SearchMovie

urlpatterns = [
	# path('', SearchMovie.as_view()),
	path('<str:searchTerm>/', Search_Result.as_view())
]