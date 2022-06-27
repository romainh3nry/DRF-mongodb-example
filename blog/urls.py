from django.urls import path
from .views import ListPerson, DetailPerson

urlpatterns = [
    path('', ListPerson.as_view(), name="movies_list"),
    path('<int:pk>', DetailPerson.as_view(), name="movie_detail")
]
