from django.urls import path
from movies_api.views import index_view, movies_data

urlpatterns = [
    path('', index_view),
    path('get-data/', movies_data, name='movies_data'),
]
